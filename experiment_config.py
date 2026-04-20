from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from dictionaries import EXPERIMENT_SCENARIO_PRESET

EXPERIMENT_MODE: bool = True

CONDITIONS = [
    "Black box",
    "SHAP",
    "Regels",
    "Tegenfeitelijk",
    "Surrogaatmodel (beslisboom)",
]

QUALTRICS_BASE_URL = "https://qualtricsxmp3nt7g5jg.qualtrics.com/jfe/form/SV_862H83gyRZHYjoa"

@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    title: str
    narrative_markdown: str
    image_path: str | None
    features: dict

SCENARIOS = [
    Scenario(
        scenario_id="S1",
        title="Scenario 1",
        narrative_markdown=(
            """### Project scenario\n"""
            "U bent betrokken als projectmanager bij een middelgroot utiliteitsproject dat zich bevindt in de voorbereidingsfase, kort vóór de start van de uitvoeringsfase.\n\n"
            "Het project betreft de nieuwbouw van een multifunctioneel gebouw in een stedelijke omgeving. De opdrachtgever is een professionele partij met meerdere interne besluitvormingslagen. Het project kent een vaste aanneemsom en wordt uitgevoerd onder UAV-GC 2025. Een deel van de werkzaamheden wordt uitbesteed aan gespecialiseerde onderaannemers.\n\n" \
            "U gebruikt een AI‑gebaseerd beslissingsondersteunend systeem dat, op basis van projectkenmerken, een inschatting geeft van het risico op vertraging. Hieronder ziet u de ingevoerde projectkenmerken, gevolgd door de voorspelling en bijbehorende uitleg.\n\n"

        ),
        image_path=None,
        features=EXPERIMENT_SCENARIO_PRESET,
    )
]

XAI_DIR = Path("XAI")

def xai_path(condition: str) -> Path:
    base = XAI_DIR
    if condition == "SHAP":
        return base / "shap.png"
    if condition == "Regels":
        return base / "rules.txt"
    if condition == "Tegenfeitelijk":
        return base / "cf.csv"
    if condition == "Surrogaatmodel (beslisboom)":
        return base / "surrogate.png"
    return base / ""  # black_box