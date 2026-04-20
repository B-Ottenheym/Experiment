import streamlit as st
import pandas as pd
import numpy as np
from data_module import generate_synthetic_data, generate_template_excel
from ml_module import train_models, generate_prediction
from xai_module import plot_global_shap, explain_global_shap, generate_local_shap, generate_counterfactuals, generate_surrogate_tree, extract_human_readable_rules
from dictionaries import binary_vars, continuous_vars, integer_continuous_vars, var_groups, var_labels_dutch, var_descriptions_dutch, group_labels_dutch, var_units_dutch, EXPERIMENT_SCENARIO_PRESET
from experiment_config import EXPERIMENT_MODE
from experiment_flow import run_experiment

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown(
    """
    <style>
        .block-container {
            max-width: 1100px;
            padding-left: 3rem;
            padding-right: 3rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if EXPERIMENT_MODE:
    run_experiment()
    st.stop()

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page_name):
    st.session_state.page = page_name

if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center; color: black;'>Explainable AI (XAI) prototype voor het voorspellen van vertragingen in bouwprojecten</h1>", unsafe_allow_html=True)
    st.write("\n\n")

    col1, col2, col3 = st.columns([2, 2, 1])
    with col2:
        st.write("")
        if st.button("Model Trainen", key="train_button"):
            go_to("train")
        st.write("")
        if st.button("Voorspellen", key="predict_button"):
            go_to("predict")

elif st.session_state.page == "train":
    st.title("Model Trainen")
    
    colA, colB, space = st.columns([1, 1, 1])
    with colA:
        if st.button("⬅ Terug naar Home"):
            go_to("home")
    with colB:
        if st.button("➡ Ga naar Voorspellen"):
            go_to("predict")
    
    train_option = st.radio(
        "Kies trainingstype:",
        ["Genereer synthetische data", "Train model met eigen data"]
    )

    if train_option == "Genereer synthetische data":
        n_samples = st.number_input(
                        label = "Aantal projecten:",
                        value=2000,
                        step=1,
                        help="Het aantal gewenste projecten in de synthetische dataset."
                        )
        if st.button("Genereer en train"):
            with st.spinner("Data genereren en modellen trainen..."):
                df, df_numerical, df_categorical, categorical_vars = generate_synthetic_data(n_samples)
                
                st.subheader("Voorbeeld van gegenereerde data (eerste 5 rijen)")
                
                df_display = df.head().rename(
                    columns=lambda c: var_labels_dutch.get(c, c)
                )
                st.dataframe(df_display)

                @st.cache_data
                def generate_csv_bytes(df):
                    return df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="Download gegenereerde data (CSV)",
                    data=generate_csv_bytes(df),
                    file_name="synthetic_project_data.csv",
                    mime="text/csv"
                )

                st.session_state.df_numerical = df_numerical
                st.session_state.df_categorical = df_categorical
                best_classifier, best_regressor, X_train_classification, y_train_classification, X_train_regression, y_train_regression, X_test_classification, X_test_regression, test_delayed, categorical_vars, numerical_cols, categorical_cols = train_models(df, df_numerical, df_categorical, categorical_vars)
            st.session_state.best_classifier = best_classifier
            st.session_state.best_regressor = best_regressor
            st.session_state.categorical_vars = categorical_vars
            st.session_state.X_test_regression = X_test_regression
            st.session_state.X_test_classification = X_test_classification
            st.session_state.X_train_classification = X_train_classification
            st.session_state.y_train_classification = y_train_classification
            st.session_state.X_train_regression = X_train_regression
            st.session_state.y_train_regression = y_train_regression
            st.session_state.numerical_cols = numerical_cols
            st.session_state.categorical_cols = categorical_cols
            st.session_state.data_prepared = True

            st.success("De modellen zijn succesvol getraind!")

            #fig, shap_order = plot_global_shap(best_regressor, X_test_classification, X_test_regression, test_delayed, categorical_vars)
            #st.pyplot(fig)

            #explain_global_shap(shap_order, var_descriptions_dutch)
            
            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button("➡ Ga naar Voorspellen", key="trainen_nr_voorspellen"):
                    go_to("predict")
            

    elif train_option == "Train model met eigen data":
        st.info("U kunt de template downloaden om te garanderen dat uw bestand de juiste structuur heeft.")


        TEMPLATE_PATH = "project_data_training_template.xlsx"

        with open(TEMPLATE_PATH, "rb") as f:
            template_bytes = f.read()

        st.download_button(
            label="Download Data Template (Excel)",
            data=template_bytes,
            file_name="project_data_training_template.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        uploaded_file = st.file_uploader("Upload Excel bestand", type=["xlsx"])
        if uploaded_file is not None:
            df_own = pd.read_excel(uploaded_file)
            st.write("Uw data:")
            st.dataframe(df_own.head())

            numerical_cols = df_own.select_dtypes(include=["int64", "float64"]).columns.tolist()
            categorical_cols = df_own.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

            target_cols = ["is_delayed", "delay_pct"]
            numerical_cols = [col for col in numerical_cols if col not in target_cols]
            categorical_cols = [col for col in categorical_cols if col not in target_cols]

            categorical_vars = {col: df_own[col].dropna().unique().tolist() for col in categorical_cols}

            df_numerical = df_own[numerical_cols]
            df_categorical = df_own[categorical_cols]
            st.session_state.df_numerical = df_numerical
            st.session_state.df_categorical = df_categorical

            best_classifier, best_regressor, X_train_classification, y_train_classification, X_train_regression, y_train_regression, X_test_classification, X_test_regression, test_delayed, categorical_vars, numerical_cols, categorical_cols = train_models(df_own, df_numerical, df_categorical, categorical_vars)
            st.session_state.best_classifier = best_classifier
            st.session_state.best_regressor = best_regressor
            st.session_state.categorical_vars = categorical_vars
            st.session_state.X_test_classification = X_test_classification
            st.session_state.X_test_regression = X_test_regression
            st.session_state.X_train_classification = X_train_classification
            st.session_state.y_train_classification = y_train_classification
            st.session_state.X_train_regression = X_train_regression
            st.session_state.y_train_regression = y_train_regression
            st.session_state.numerical_cols = numerical_cols
            st.session_state.categorical_cols = categorical_cols
            st.session_state.data_prepared = True

            fig, shap_order = plot_global_shap(best_regressor, X_test_classification, X_test_regression, test_delayed, categorical_vars)
            st.pyplot(fig)

            explain_global_shap(shap_order, var_descriptions_dutch)

            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button("➡ Ga naar Voorspellen", key="trainen_nr_voorspellen2"):
                    go_to("predict")

elif st.session_state.page == "predict":
    st.title("Voorspellen")
    if st.button("⬅ Terug naar Home"):
        go_to("home")

    if st.button("📄 Laad experimenteel projectschema"):
        st.session_state.loaded_scenario = EXPERIMENT_SCENARIO_PRESET.copy()
        st.success("Experimenteel scenario geladen.")

    st.write("Voer hieronder de projectdetails in:")

    if "best_classifier" not in st.session_state or "best_regressor" not in st.session_state:
        st.warning("Train eerst de modellen.")
        if st.button("➡ Ga naar Model Trainen"):
                go_to("train")
    else:
        user_inputs_num = {}
        user_inputs_cat = {}

        scenario = st.session_state.get("loaded_scenario", {})

        st.subheader("Projectcontext")

        default_duration = scenario.get("planned_project_duration_days", 365)
        user_inputs_num["planned_project_duration_days"] = st.number_input(
            "Geplande projectduur (dagen)",
            min_value=1,
            value=int(default_duration),
            step=1,
            help="Geplande totale looptijd van het project in kalenderdagen."
        )

        for section, variables in var_groups.items():
            dutch_label = group_labels_dutch.get(section, section)
            st.subheader(dutch_label)

            for var in variables:
                base_label = var_labels_dutch.get(var, var)
                unit = var_units_dutch.get(var)

                if unit:
                    label = f"{base_label} ({unit})"
                else:
                    label = base_label

                tooltip = var_descriptions_dutch.get(var)

                if var in st.session_state.df_numerical.columns:         
                    default_value = scenario.get(
                        var,
                        st.session_state.df_numerical[var].mean()
                    )

                    if var in binary_vars:
                        binary_value = scenario.get(var, default_value)
                        index = 1 if binary_value == 1 else 0

                        choice = st.selectbox(
                            label,
                            options=["Nee", "Ja"],
                            index=index,
                            help=tooltip,
                        )

                        user_inputs_num[var] = 1 if choice == "Ja" else 0

                    elif var in integer_continuous_vars and var in continuous_vars:
                        mu, sigma, min_v, max_v = continuous_vars[var]
                        user_inputs_num[var] = st.number_input(
                            label,
                            min_value=int(min_v),
                            max_value=int(max_v),
                            value=int(round(default_value)),
                            step=1,
                            format="%d",
                            help=tooltip,
                        )

                    elif var in continuous_vars:
                        mu, sigma, min_v, max_v = continuous_vars[var]
                        user_inputs_num[var] = st.number_input(
                            label,
                            min_value=float(min_v),
                            max_value=float(max_v),
                            value=round(float(default_value), 1),
                            step=0.1,
                            format="%.1f",
                            help=tooltip,
                        )

                elif var in st.session_state.df_categorical.columns:
                    if var in st.session_state.categorical_vars:
                        options = st.session_state.categorical_vars[var][0]
                        if var in scenario:
                            default_index = options.index(scenario[var])
                        else:
                            default_index = 0
                        user_inputs_cat[var] = st.selectbox(label, options, index=default_index, help=tooltip)

        input_data_dict = {**user_inputs_num, **user_inputs_cat}
        input_data = pd.DataFrame({k: [v] for k, v in input_data_dict.items()})
        
        num_cols_present = [c for c in st.session_state.numerical_cols if c in input_data.columns]
        cat_cols_present = [c for c in st.session_state.categorical_cols if c in input_data.columns]
        
        input_num = input_data[num_cols_present] if num_cols_present else pd.DataFrame()
        input_cat = input_data[cat_cols_present] if cat_cols_present else pd.DataFrame()
        
        if len(cat_cols_present) > 0:
            input_cat_encoded = pd.get_dummies(input_cat, columns=cat_cols_present, drop_first=True)
            input_encoded = pd.concat([input_num, input_cat_encoded], axis=1)
        else:
            input_encoded = input_num
            
        input_encoded = input_encoded.reindex(columns=st.session_state.X_train_classification.columns, fill_value=0).astype(float)

        if st.button("Voorspellen"):
            result = generate_prediction(
                input_data=input_data,
                best_classifier=st.session_state.best_classifier,
                best_regressor=st.session_state.best_regressor,
                categorical_vars=st.session_state.categorical_vars,
                X_test_classification_columns=st.session_state.X_test_classification.columns,
                X_test_regression_columns=st.session_state.X_test_regression.columns,
                planned_duration_days = input_data["planned_project_duration_days"].iloc[0]
            )
            st.session_state.predicted_severity = result['predicted_severity']

            st.write("### Voorspellingsresultaten")
            st.write(f"Waarschijnlijkheid van vertraging: {result['probability_delay'] * 100:.1f}%")
            st.write(f"Ernst van vertraging: {result['predicted_severity'] * 100:.1f}%")
            st.write(f"Verwachte vertraging (waarschijnlijkheid x ernst): {result['expected_delay_pct'] * 100:.1f}%")
            st.write(f"Verwachte vertraging: {int(round(result['expected_delay_days']))} dagen")

            st.write("### Lokale SHAP verklaring")

            generate_local_shap(
                shap_explainer=st.session_state.shap_explainer_classification, 
                input_encoded=input_encoded, 
                X_test_classification=st.session_state.X_test_classification, 
                categorical_vars=st.session_state.categorical_vars)

            @st.fragment
            def cf():
                st.write("### Tegenfeitelijke verklaring (Actiegerichte wat-als-uitleg)")

                with st.expander("Wat zijn tegenfeitelijke verklaringen?"):
                    st.markdown("""
                    **Tegenfeitelijke verklaringen laten zien hoe u waarden van projectkenmerken kunt wijzigen om de voorspelling van het model te beinvloeden.**
                    - Het systeem genereert automatisch tegenfeitelijke varianten om de voorspelde vertraging te minimaliseren.
                    - De tabel toont de oorspronkelijke waarde, de tegenfeitelijke waarde en het verschil.
                    - Boven de tabel wordt de nieuw voorspelde ernst van vertraging weergegeven.
                    """)


                if 'selected_features' not in st.session_state:
                    st.session_state.selected_features = []

                current_pred = st.session_state.predicted_severity
                st.info(f"📊 **Huidge voorspelde vertragingsernst: {result['predicted_severity'] * 100:.1f}%**")

                
                generate_counterfactuals(
                    X_train_regression=st.session_state.X_train_regression,
                    y_train_regression=st.session_state.y_train_regression,
                    best_regressor=st.session_state.best_regressor,
                    input_encoded=input_encoded,
                    shap_top_features=st.session_state.shap_top_features_raw,
                )
            cf()

            st.write("### Globale beslisstructuur (surrogaatmodel)")
            surrogate, categorical_dummy_lookup = generate_surrogate_tree(
                black_box_model=st.session_state.best_classifier,
                X_train=st.session_state.X_train_classification,
            )

            predicted_label = ("vertraagd" if result["delay_class"] == 1 else "niet vertraagd")

            st.write("### Regel-gebaseerde verklaring")
            st.markdown(
                f"**Dit project wordt voorspeld als _{predicted_label}_ op basis van de volgende beslisregels:**"
            )

            rules = extract_human_readable_rules(
                surrogate=surrogate,
                feature_names=st.session_state.X_train_classification.columns,
                x_instance=input_encoded.values,
                var_labels_dutch=var_labels_dutch,
                var_units_dutch=var_units_dutch,
                categorical_vars=st.session_state.categorical_vars,
                categorical_dummy_lookup=categorical_dummy_lookup,
                binary_vars=binary_vars
            )

            for rule in rules:
                st.markdown(f"- {rule}")