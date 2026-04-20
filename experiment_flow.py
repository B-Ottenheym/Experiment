from __future__ import annotations
import uuid
import urllib.parse
from dataclasses import asdict
import html
import pandas as pd
import streamlit as st
import numpy as np
import json
from pathlib import Path
import random
from dictionaries import var_groups, var_labels_dutch, var_descriptions_dutch, var_units_dutch, group_labels_dutch, binary_vars
from experiment_config import (CONDITIONS, QUALTRICS_BASE_URL, SCENARIOS, xai_path, XAI_DIR)

CONDITION_COUNT_FILE = Path("condition_counts.json")

def _init_participant_state():
    if "pid" not in st.session_state: #participant id
        st.session_state.pid = str(uuid.uuid4())
    if "scenario_id" not in st.session_state:
        st.session_state.scenario_id = SCENARIOS[0].scenario_id
    if "condition" not in st.session_state:
        st.session_state.condition = assign_condition(CONDITIONS)
    if "exp_step" not in st.session_state:
        st.session_state.exp_step = 1

def _get_scenario():
    sid = st.session_state.scenario_id
    for s in SCENARIOS:
        if s.scenario_id == sid:
            return s
    return SCENARIOS[0]

def _next():
    st.session_state.exp_step += 1

def _back():
    st.session_state.exp_step = max(1, st.session_state.exp_step - 1)

def _progress():
    st.progress((st.session_state.exp_step - 1) / 4)
    st.caption(f"Stap {st.session_state.exp_step} van 4")

def _build_qualtrics_url():
    params = {
        "pid": st.session_state.pid,
        "cond": st.session_state.condition,
    }
    qs = urllib.parse.urlencode(params)
    if "?" in QUALTRICS_BASE_URL:
        return QUALTRICS_BASE_URL + "&" + qs
    return QUALTRICS_BASE_URL + "?" + qs

def assign_condition(conditions: list[str]) -> str:
    if CONDITION_COUNT_FILE.exists():
        counts = json.loads(CONDITION_COUNT_FILE.read_text())
    else:
        counts = {c: 0 for c in conditions}

    min_count = min(counts.values())
    candidates = [c for c, n in counts.items() if n == min_count]

    condition = random.choice(candidates)

    counts[condition] += 1
    CONDITION_COUNT_FILE.write_text(json.dumps(counts, indent=2))

    return condition

def _features_to_table(features: dict) -> pd.DataFrame:
    rows = []

    grouped_vars = {v for vs in var_groups.values() for v in vs}

    for group, vars_ in var_groups.items():
        group_label = group_labels_dutch.get(group, group)

        for v in vars_:
            if v not in features:
                continue

            label = var_labels_dutch.get(v, v)
            unit = var_units_dutch.get(v)
            if unit:
                label = f"{label} ({unit})"

            waarde = features[v]
            if isinstance(waarde, (int, np.integer)) and v in binary_vars:
                waarde = "Ja" if waarde == 1 else "Nee"

            rows.append({
                "Categorie": group_label,
                "Variabele": label,
                "Waarde": waarde,
                "Beschrijving": var_descriptions_dutch.get(v, ""),
            })

    for k, val in features.items():
        if k in grouped_vars:
            continue

        label = var_labels_dutch.get(k, k)
        unit = var_units_dutch.get(k)
        if unit:
            label = f"{label} ({unit})"

        rows.append({
            "Categorie": "Overig",
            "Variabele": label,
            "Waarde": val,
            "Beschrijving": var_descriptions_dutch.get(k, ""),
        })

    df = pd.DataFrame(rows)

    df["Categorie"] = df["Categorie"].where(
        df["Categorie"].ne(df["Categorie"].shift()),
        ""
    )

    return df

def step_1_consent():
    st.header("Welkom")
    st.markdown(
        """
In dit onderzoek maakt u kennis met een prototype van een AI‑gebaseerd
beslissingsondersteunend systeem voor bouwprojecten.

U krijgt een projectsituatie te zien, samen met een voorspelling van het risico op
projectvertraging die door het systeem wordt gegenereerd. Afhankelijk van de versie
van het systeem die u te zien krijgt, wordt deze voorspelling mogelijk ondersteund
door aanvullende uitleg.

Tijdens het experiment wordt u gevraagd om de informatie die het systeem presenteert
zorgvuldig te bekijken. Het onderzoek richt zich niet op het nemen van beslissingen,
maar op **uw perceptie van de uitkomsten van het systeem en de bijbehorende uitleg**.

Het experiment bestaat uit enkele korte stappen en neemt slechts enkele minuten in
beslag. Na afloop wordt u automatisch doorgestuurd naar een vragenlijst waarin u wordt
gevraagd uw ervaringen met het systeem te beoordelen.

Uw deelname is vrijwillig en uw antwoorden worden anoniem verwerkt. U kunt op elk
moment stoppen met het experiment zonder opgave van reden.
"""
    )

    consent = st.checkbox(
        "Ik heb de bovenstaande informatie gelezen en ga akkoord met deelname aan dit onderzoek."
    )

    col1, col2 = st.columns([1, 1])
    with col2:
        st.button("Volgende", key="step1_next", disabled=not consent, on_click=_next)

def step_2_assignment():
    st.header("Uitleg van het systeem")

    st.markdown(
        """
In de volgende stap krijgt u een projectsituatie te zien, samen met een voorspelling
van het risico op projectvertraging die door een AI‑systeem wordt gegenereerd.

U bent toegewezen aan een specifieke versie van het systeem. Deze versie verschilt in
de manier waarop de voorspelling wordt toegelicht. Hieronder wordt kort uitgelegd hoe
de uitleg in uw versie is opgebouwd.
"""
    )

    cond = st.session_state.condition
    st.info(f"Toegewezen versie: **{st.session_state.condition}**")
    if cond == "Black box":
        st.info(
            """
**In deze versie van het systeem wordt alleen de voorspelling getoond.**

Er wordt geen aanvullende uitleg gegeven over hoe het systeem tot deze voorspelling
is gekomen.
"""
        )

    elif cond == "SHAP":
        st.info(
            """
**In deze versie van het systeem wordt de voorspelling ondersteund door een visuele uitleg.**

De uitleg laat zien welke projectkenmerken volgens het systeem het meest hebben
bijgedragen aan de voorspelling, en in welke mate deze kenmerken het risico op
vertraging verhogen of verlagen.
"""
        )

    elif cond == "Regels":
        st.info(
            """
**In deze versie van het systeem wordt de voorspelling toegelicht met behulp van regels.**

Deze regels beschrijven combinaties van projectkenmerken waarvoor de voorspelling
geldig is. De uitleg geeft inzicht in welke voorwaarden doorslaggevend zijn geweest
voor de uitkomst.
"""
        )

    elif cond == "Tegenfeitelijk":
        st.info(
            """
**In deze versie van het systeem wordt de voorspelling toegelicht met alternatieve scenario’s.**

De uitleg laat zien hoe kleine aanpassingen in specifieke projectkenmerken zouden
kunnen leiden tot een andere voorspelling, bijvoorbeeld een lager risico op
vertraging.
"""
        )

    elif cond == "Surrogaatmodel (beslisboom)":
        st.info(
            """
**In deze versie van het systeem wordt de voorspelling toegelicht met een vereenvoudigd model.**

Dit model geeft een overzicht van de belangrijkste beslisregels die het AI‑systeem
gebruikt om tot een voorspelling te komen, in een vorm die makkelijker te interpreteren is.
"""
        )

    st.markdown(
        """
Lees deze uitleg zorgvuldig door. In de volgende stap ziet u de projectsituatie en
kunt u de voorspelling en bijbehorende uitleg bekijken.
"""
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("Terug", key="step2_back", on_click=_back)
    with col2:
        st.button("Volgende", key="step2_next", on_click=_next)

def step_3_scenario():
    scenario = _get_scenario()
    st.header("Scenario en voorspelling")
    st.markdown(scenario.narrative_markdown)

    if scenario.image_path:
        try:
            st.image(scenario.image_path, use_container_width=True)
        except Exception:
            st.warning("De scenario-afbeelding kon niet worden geladen.")

    st.markdown("#### Projectkenmerken")
    df = _features_to_table(scenario.features)
    st.dataframe(df, use_container_width=True, hide_index=True, 
        column_config={
                "Categorie": st.column_config.TextColumn(
                    "Categorie", width=240),
                "Variabele": st.column_config.TextColumn(
                    "Variabele", width=460),
                "Waarde": st.column_config.TextColumn(
                    "Waarde", width=100),
                "Beschrijving": st.column_config.TextColumn(
                    "Beschrijving", width=950)
                ,}
        )

    st.markdown("---")
    st.markdown(
        """Hieronder kunt u op **Voorspellen** klikken om de AI‑uitkomst en de bijbehorende uitleg te bekijken.

De invoerwaarden zijn vastgezet voor dit onderzoek en kunnen niet worden aangepast."""
    )

    if "show_results" not in st.session_state:
        st.session_state.show_results = False

    if st.button("Voorspellen", key="step3_predict",):
        st.session_state.show_results = True

    if st.session_state.show_results:
        st.subheader("AI‑uitkomst")

        prediction_path = XAI_DIR / "prediction.txt"

        if prediction_path.exists():
            text = html.unescape(prediction_path.read_text(encoding="utf-8"))

            for line in text.splitlines():
                line = line.strip()
                if not line:
                    st.markdown("")
                    continue

                if ":" in line:
                    left, right = line.split(":", 1)
                    st.markdown(f"{left}: **{right.strip()}**")
                else:
                    st.markdown(f"**{line}**")
            st.markdown(
                "*Deze voorspelling geeft de **verwachte impact van het risico op projectvertraging** weer. "
                "Het AI‑model combineert de kans op vertraging met de verwachte ernst ervan ten opzichte van de geplande projectduur.*"
                )
        else:
            st.warning(f"Voorspellingsbestand niet gevonden: {prediction_path}")



        st.subheader("Uitleg")
        cond = st.session_state.condition

        if cond == "Black box":
            st.info("In deze versie van het systeem wordt geen uitleg bij de voorspelling gegeven.")

        elif cond in ("SHAP", "Surrogaatmodel (beslisboom)"):
            p = xai_path(cond)
            if p.exists():
                st.image(str(p), use_container_width=True)
            else:
                st.warning(f"Afbeelding niet gevonden: {p}")

        elif cond == "Regels":
            p = xai_path(cond)
            if p.exists():
                text = html.unescape(p.read_text(encoding="utf-8"))

                lines = [l.strip() for l in text.splitlines() if l.strip()]

                st.markdown("**Deze voorspelling wordt toegelicht met behulp van de volgende beslisregels:**")
                st.markdown(
                    "\n".join(f"- {line}" for line in lines[1:])
                )
            else:
                st.warning(f"Regels niet gevonden: {p}")

        elif cond == "Tegenfeitelijk":
            p = xai_path(cond)
            if p.exists():
                df = pd.read_csv(p, sep=";")

                for col in ["Origineel", "Tegenfeitelijk", "Verschil"]:
                    df[col] = (
                        df[col]
                        .astype(str)
                        .str.replace(",", ".", regex=False)
                        .astype(float)
                    )

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.warning(f"Tabel niet gevonden: {p}")


        if cond == "SHAP":
            with st.expander("Wat betekent deze grafiek?"):
                st.markdown("""
                Deze grafiek laat zien **welke projectkenmerken volgens het model de grootste invloed hebben**
                op de voorspelling voor **dit specifieke project**.

                - Balken die **omhoog** wijzen geven kenmerken aan die het risico op vertraging **verhogen**.
                - Balken die **omlaag** wijzen geven kenmerken aan die het risico op vertraging **verlagen**.
                - De lengte van de balk geeft aan **hoe groot die invloed is**.

                Dit is een **lokale uitleg**:  
                deze verklaart alleen de voorspelling van dit project, niet van alle projecten in de dataset.
                """)

        elif cond == "Regels":
            with st.expander("Wat betekent deze uitleg?"):
                st.markdown("""
                Deze uitleg toont een regel die laat zien hoe het AI‑model tot deze voorspelling komt.
                            
                **Wat laat deze regel zien?**
                De regel geeft aan dat **zodra deze combinatie van projectkenmerken aanwezig is**, het model doorgaans een vergelijkbare voorspelling geeft als bij dit project.
                
                **Hoe leest u deze regel?**
                Als aan alle genoemde voorwaarden wordt voldaan, dan hoort daar volgens het model deze inschatting van de verwachte vertraging bij.

                Zie dit als:  
                *Dit zijn de belangrijkste kenmerken waarop het model zich baseert om deze voorspelling te maken.*
                """)

        elif cond == "Tegenfeitelijk":
            with st.expander("Wat betekent deze uitleg?"):
                st.markdown("""
                    Dit tegenfeitelijk scenario laat zien welke aanpassingen in het project zouden leiden tot een duidelijk 
                    lager vertragingsrisico volgens het model.\n\n

                    De uitleg laat dus zien **welke veranderingen volgens het model relevant zijn** voor de voorspelling.
                    """)

        elif cond == "Surrogaatmodel (beslisboom)":
            with st.expander("Wat betekent deze uitleg?"):
                st.markdown("""
                    Deze beslisboom is een **vereenvoudigde weergave** van hoe het AI‑model
                    in grote lijnen tot een voorspelling komt.

                    - De boom **benadert** het gedrag van het oorspronkelijke model, maar is niet hetzelfde.
                    - Hij laat zien **welke projectkenmerken vaak als eerste worden gebruikt** bij het maken van een inschatting.

                    Zie dit als:  
                    *Een globale indruk van hoe het model redeneert.*
                    """)

    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("Terug", key="step3_back", on_click=_back)
    with col2:
        st.button(
            "Doorgaan naar vragenlijst", key="step3_next",
            disabled=not st.session_state.get("show_results", False),
            on_click=_next
        )

def step_4_redirect():
    st.header("Vragenlijst")
    st.markdown(
        """Klik op de knop hieronder om door te gaan naar de vragenlijst.\n\n"""
    )
    url = _build_qualtrics_url()
    st.link_button("Open vragenlijst", url)
    st.caption("Werkt de knop niet? Kopieer dan de onderstaande link en plak deze in uw browser.")
    st.code(url, language="text")

def run_experiment():
    _init_participant_state()
    _progress()

    step = st.session_state.exp_step
    if step == 1:
        step_1_consent()
    elif step == 2:
        step_2_assignment()
    elif step == 3:
        step_3_scenario()
    else:
        step_4_redirect()