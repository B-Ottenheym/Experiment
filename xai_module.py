import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import dice_ml
from dictionaries import var_descriptions_dutch, var_labels_dutch, continuous_vars, integer_continuous_vars, continuous_directionality, continuous_actionable, binary_actionable, binary_vars, var_units_dutch, categorical_vars
from sklearn.tree import DecisionTreeClassifier, plot_tree
from graphviz import Digraph

def plot_global_shap(best_regressor, X_test_classification, X_test_regression, test_delayed, categorical_vars):
    predicted_severity = np.zeros(len(X_test_classification))
    predicted_severity[test_delayed.reset_index(drop=True).index] = best_regressor.predict(X_test_regression)

    explainer_cls = st.session_state.shap_explainer_classification
    shap_values_cls = explainer_cls(X_test_classification)

    explainer_reg = st.session_state.shap_explainer_regression
    shap_values_reg = explainer_reg(X_test_regression)

    shap_cls_values = shap_values_cls.values
    if shap_cls_values.ndim == 3:
        shap_cls_values = shap_cls_values[..., 1]

    shap_reg_values = shap_values_reg.values
    if shap_reg_values.ndim > 2:
        shap_reg_values = shap_reg_values[..., 0]

    expected_shap_values = np.zeros_like(shap_cls_values)
    delayed_mask = X_test_classification.index.isin(test_delayed.index)
    delayed_idx = np.where(delayed_mask)[0]

    expected_shap_values[delayed_idx] = (
        shap_cls_values[delayed_idx] * predicted_severity[delayed_idx, None]
        + shap_reg_values
    )

    shap_df = pd.DataFrame(expected_shap_values, columns=X_test_classification.columns)

    for cat_var in categorical_vars.keys():
        one_hot_cols = [col for col in X_test_classification.columns if col.startswith(cat_var + "_")]
        if one_hot_cols:
            shap_df[cat_var] = shap_df[one_hot_cols].sum(axis=1)
            shap_df.drop(columns=one_hot_cols, inplace=True)

    renamed_cols = [var_labels_dutch.get(col, col) for col in shap_df.columns]
    shap_df.columns = renamed_cols

    plot_shap_df = shap_df.drop(columns=[col for col in shap_df.columns if col.startswith("project_type")], errors='ignore')
    mean_shap = plot_shap_df.abs().mean().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10,6))
    mean_shap.plot.bar(ax=ax, color="#ffab72ff")
    ax.set_title("Globale SHAP-waarden")
    ax.set_ylabel("Gemiddelde SHAP-waarde")
    plt.tight_layout()

    return fig, mean_shap.index.tolist()

def explain_global_shap(mean_shap_order, feature_descriptions):
    with st.expander("Wat betekent deze grafiek?"):
        st.markdown("""
        **Deze grafiek laat zien welke factoren de grootste invloed hebben op projectvertragingen binnen alle projecten in uw dataset.**

        - Elke balk vertegenwoordigd een factor die de voorspelde vertraging beïnvloedt.
        - Hogere balken = grotere impact op de voorspelling.
        - De waarden (SHAP-waarden) vertegenwoordigen het **gemiddelde effect** van elke factor.
        - De grafiek toont **hoe belangrijk** elke factor is, maar geeft **niet aan in welke richting** het effect werkt (dus niet of de vertraging toeneemt of afneemt). Dit is wel te zien in de **lokale SHAP-grafiek** op de **Voorspellen** pagina.
        - Dit is een **globale verklaring**, wat betekent dat het de werking van het model voor alle projecten in de dataset samenvat, en niet slechts één specifiek project.                  
        """)
    with st.expander("Uitleg variabelen"):
        for feature in mean_shap_order:
            description = feature_descriptions.get(feature)
            st.markdown(f"**{feature}**: {description}")

def generate_counterfactuals(
    X_train_regression,
    y_train_regression,
    best_regressor,
    input_encoded,
    shap_top_features,
):

    MAX_FEATURES_TO_VARY = 10

    numeric_features = [
        c for c in continuous_vars.keys()
        if c in X_train_regression.columns
    ]

    integer_features = set(integer_continuous_vars)
    
    decimal_features = {
        c for c in continuous_vars
        if c not in integer_features
    }

    features_to_vary = [
        f for f in numeric_features
        if f in input_encoded.columns
    ][:MAX_FEATURES_TO_VARY]

    if not features_to_vary:
        st.warning("Geen tegenfeitelijke varianten gevonden.")
        return

    permitted_range = {}
    query_instance = input_encoded.iloc[[0]]

    for col in features_to_vary:
        orig_val = float(query_instance[col].iloc[0])

        if col in continuous_vars:
            _, _, min_v, max_v = continuous_vars[col]
        else:
            min_v = float(X_train_regression[col].min())
            max_v = float(X_train_regression[col].max())

        if col in continuous_directionality:
            direction = continuous_directionality[col]

            if direction == -1:
                mn = orig_val
                mx = max_v
            elif direction == +1:
                mn = min_v
                mx = orig_val
            else:
                mn, mx = min_v, max_v
        else:
            mn, mx = min_v, max_v

        if mn < mx:
            if col in integer_features:
                permitted_range[col] = [int(np.floor(mn)), int(np.ceil(mx))]
            else:
                permitted_range[col] = [float(mn), float(mx)]


    Xy_train = X_train_regression.copy()
    Xy_train["delay_pct"] = y_train_regression

    data_dice = dice_ml.Data(
        dataframe=Xy_train,
        continuous_features=numeric_features,
        categorical_features=[],
        outcome_name="delay_pct"
    )

    model_dice = dice_ml.Model(
        model=best_regressor,
        backend="sklearn",
        model_type="regressor"
    )

    exp = dice_ml.Dice(data_dice, model_dice, method="random")

    current_pred = float(best_regressor.predict(query_instance)[0])

    STEP = 0.05
    START_FACTOR = 0.95
    MIN_FACTOR = 0.05
    MAX_ITERS = int((START_FACTOR - MIN_FACTOR) / STEP) + 1

    all_cf_candidates = []
    best_target_upper = None

    factor = START_FACTOR


    FEATURE_SCHEDULE = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, len(features_to_vary)]

    for _ in range(MAX_ITERS):
        desired_upper = current_pred * factor
        cf_df = None

        for k in FEATURE_SCHEDULE:
            try:
                dice_exp = exp.generate_counterfactuals(
                    query_instance,
                    total_CFs=40,
                    features_to_vary=features_to_vary[:k],
                    permitted_range=permitted_range,
                    desired_range=[0, desired_upper],
                    verbose=False,
                )
            except Exception:
                continue

            cf_df = dice_exp.cf_examples_list[0].final_cfs_df
            if cf_df is not None and not cf_df.empty:
                break

        if cf_df is None or cf_df.empty:
            break


        cf_df = dice_exp.cf_examples_list[0].final_cfs_df

        if cf_df is None or cf_df.empty:
            break

        cf_df = cf_df.drop(columns=["delay_pct"], errors="ignore")

        for col in cf_df.columns:
            if col in integer_features:
                cf_df[col] = np.round(cf_df[col]).astype(int)
            elif col in decimal_features:
                cf_df[col] = cf_df[col].round(1)

        preds = best_regressor.predict(cf_df[input_encoded.columns])
        cf_df["predicted_delay"] = preds

        cf_df = cf_df[cf_df["predicted_delay"] < current_pred]

        if cf_df.empty:
            break

        all_cf_candidates.append(cf_df.copy())
        best_target_upper = desired_upper

        factor -= STEP

    if not all_cf_candidates:
        st.warning("Geen betere tegenfeitelijke varianten gevonden.")
        return
    
    orig = query_instance.iloc[0] 
    cf_df = pd.concat(all_cf_candidates, ignore_index=True)
    cf_df = cf_df.drop_duplicates(subset=input_encoded.columns.tolist())
    cf_df["n_changes"] = cf_df.apply(
        lambda row: sum(
            not np.isclose(orig[col], row[col])
            for col in features_to_vary
        ),
        axis=1
    )

    cf_df = cf_df.sort_values(
        ["predicted_delay", "n_changes"]
    ).head(3)

    if best_target_upper is not None:
        improvement_pct = (1 - (best_target_upper / current_pred)) * 100 if current_pred > 0 else 0
        st.info(f"✅ Beste haalbare reductie gevonden: ongeveer **{improvement_pct:.0f}%** (target ≤ {best_target_upper:.3f}).")


    if cf_df is None or cf_df.empty:
        st.warning("Geen betere tegenfeitelijke varianten gevonden.")
        return

    cf_df = cf_df.drop(columns=["delay_pct"], errors="ignore")

    for col in cf_df.columns:
        if col in integer_features:
            cf_df[col] = np.round(cf_df[col]).astype(int)

    preds = best_regressor.predict(cf_df[input_encoded.columns])
    cf_df["predicted_delay"] = preds

    cf_df = cf_df[cf_df["predicted_delay"] < current_pred]

    cf_df = cf_df.sort_values("predicted_delay").head(3)


    def label_with_unit(var: str) -> str:
        label = var_labels_dutch.get(var, var)
        unit = var_units_dutch.get(var)

        if unit:
            return f"{label}\n({unit})" 
        return label

    for i, cf in cf_df.iterrows():
        st.markdown(
            f"### Tegenfeitelijke variant – voorspelde vertraging: **{cf['predicted_delay']:.3f}**"
        )

        changed_all = []
        for col in features_to_vary:
            if not np.isclose(orig[col], cf[col]):
                changed_all.append(col)

        changed_actionable = [
            c for c in changed_all
            if c in continuous_actionable or c in binary_actionable
        ]
    
        display = pd.DataFrame(
            {
                "Variabele": [label_with_unit(c) for c in changed_actionable],
                "Origineel": [orig[c] for c in changed_actionable],
                "Tegenfeitelijk": [cf[c] for c in changed_actionable],
                "Verschil": [cf[c] - orig[c] for c in changed_actionable],
            }
        )

        st.dataframe(display, hide_index=True)

def generate_local_shap(
    shap_explainer,
    input_encoded,
    X_test_classification,
    categorical_vars,
):
    shap_values = shap_explainer(input_encoded)

    if shap_values.values.ndim == 3:
        shap_array = shap_values.values[:, :, 1]
    else:
        shap_array = shap_values.values

    shap_df = pd.DataFrame(
        shap_array,
        columns=X_test_classification.columns
    )

    for cat_var in categorical_vars.keys():
        one_hot_cols = [
            col for col in shap_df.columns
            if col.startswith(cat_var + "_")
        ]
        if one_hot_cols:
            shap_df[cat_var] = shap_df[one_hot_cols].sum(axis=1)
            shap_df.drop(columns=one_hot_cols, inplace=True)

    local_values_raw = shap_df.iloc[0]

    TOP_K = 15
    shap_top_raw = (
        local_values_raw
        .abs()
        .sort_values(ascending=False)
        .head(TOP_K)
        .index
        .tolist()
    )

    st.session_state.shap_top_features_raw = shap_top_raw

    def format_label_with_unit(var):
        label = var_labels_dutch.get(var, var)
        unit = var_units_dutch.get(var)
        if unit:
            return f"{label} ({unit})"
        return label

    shap_df_vis = shap_df.copy()
    shap_df_vis.columns = [
        format_label_with_unit(col)
        for col in shap_df_vis
    ]

    local_values_vis = shap_df_vis.iloc[0]

    shap_top_vis = (
        local_values_vis
        .reindex(
            local_values_vis.abs()
            .sort_values(ascending=False)
            .head(TOP_K)
            .index
        )
    )

    fig, ax = plt.subplots(figsize=(10, 4))

    shap_top_vis.plot.bar(
        ax=ax,
        color="#ffab72ff"
    )

    ax.axhline(
        y=0,
        color="black",
        linewidth=0.8,
        alpha=0.6
    )
    
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        ha="right",
        va="top",
        rotation_mode="anchor"
    )
    
    ax.set_title("Top 20 lokale SHAP-bijdragen")
    ax.set_ylabel("SHAP-waarde")

    st.pyplot(fig)
    plt.close(fig)

    with st.expander("Wat betekent deze grafiek?"):
        st.markdown("""
        **Deze grafiek toont welke factoren de grootste invloed hebben op de voorspelde projectvertraging
        voor dit specifieke project.**

        - Balken **boven nul** vergroten de voorspelde vertraging.
        - Balken **onder nul** verlagen de voorspelde vertraging.
        - De lengte van de balk geeft de relatieve invloed weer.
        - Dit betreft een **lokale verklaring** (alleen dit project).
        """)

    with st.expander("Uitleg variabelen"):
        for key, label in var_labels_dutch.items():
            description = var_descriptions_dutch.get(key)
            if description:
                st.markdown(f"**{label}**: {description}")

def generate_surrogate_tree(
    black_box_model,
    X_train,
    max_depth=3
):
    
    categorical_dummy_lookup = {}
    for col in st.session_state.X_train_classification.columns:
        for base_var in categorical_vars.keys():
            prefix = base_var + "_"
            if col.startswith(prefix):
                active_cat = col[len(prefix):]
                categorical_dummy_lookup[col] = (base_var, active_cat)

    def render_human_tree(
        tree,
        feature_names,
        var_labels_dutch,
        binary_vars,
        categorical_vars,
        categorical_dummy_lookup
    ):
        dot = Digraph()
        dot.attr(rankdir="TB", fontname="Helvetica")

        def recurse(node):
            if tree.feature[node] == -2:
                counts = tree.value[node][0]          # aantallen per klasse
                total = counts.sum()
                prob_delay = (counts[1] / total) if total > 0 else 0.0

                pred_class = int(np.argmax(counts))   # 0 of 1
                is_delay = (pred_class == 1)

                label = f"Vertraging" if is_delay else f"Geen vertraging"
                color = "#f8d7da" if is_delay else "#d4edda"
                border = "#a94442" if is_delay else "#3c763d"

                dot.node(
                    str(node),
                    label,
                    shape="box",
                    style="filled",
                    fillcolor=color,
                    color=border,
                    fontname="Helvetica-Bold"
                )
                return

            feature = feature_names[tree.feature[node]]

            if feature in categorical_dummy_lookup:
                base_var, active_cat = categorical_dummy_lookup[feature]

                pretty = var_labels_dutch.get(base_var, base_var)
                unit = var_units_dutch.get(base_var, "")
                label = f"{pretty}\n({unit})" if unit else pretty

                dot.node(str(node), label, shape="box")

                all_cats = categorical_vars[base_var][0]
                other_cats = [c for c in all_cats if c != active_cat]

                left_label = " / ".join(other_cats)
                right_label = active_cat

                left = tree.children_left[node]
                right = tree.children_right[node]

                dot.edge(str(node), str(left), label=left_label)
                dot.edge(str(node), str(right), label=right_label)

            else:
                pretty = var_labels_dutch.get(feature, feature)
                unit = var_units_dutch.get(feature, "")
                label = f"{pretty}\n({unit})" if unit else pretty
                dot.node(str(node), label, shape="box")

                left = tree.children_left[node]
                right = tree.children_right[node]

                if feature in binary_vars:
                    dot.edge(str(node), str(left), label="Nee")
                    dot.edge(str(node), str(right), label="Ja")
                else:
                    threshold = tree.threshold[node]
                    dot.edge(str(node), str(left), label=f"< {threshold:.0f}")
                    dot.edge(str(node), str(right), label=f"≥ {threshold:.0f}")

            recurse(left)
            recurse(right)

        recurse(0)
        return dot

    y_surrogate = (black_box_model.predict(X_train) > 0.5).astype(int)

    surrogate = DecisionTreeClassifier(
        max_depth=max_depth,
        random_state=58, #58 #76
        max_features="sqrt",
        min_samples_leaf=30,
        min_samples_split=60,
        class_weight="balanced",
        min_impurity_decrease=0.001
    )

    surrogate.fit(X_train, y_surrogate)

    dot = render_human_tree(
        surrogate.tree_,
        X_train.columns,
        var_labels_dutch,
        binary_vars,
        categorical_vars,
        categorical_dummy_lookup
    )

    st.graphviz_chart(dot)

    return surrogate, categorical_dummy_lookup

def extract_human_readable_rules(
    surrogate,
    feature_names,
    x_instance,
    var_labels_dutch,
    var_units_dutch,
    categorical_vars,
    categorical_dummy_lookup,
    binary_vars
):

    tree = surrogate.tree_
    node_indicator = surrogate.decision_path(x_instance)
    leaf_id = surrogate.apply(x_instance)

    rules = []

    for node_id in node_indicator.indices:
        if leaf_id[0] == node_id:
            continue

        feature_idx = tree.feature[node_id]
        threshold = tree.threshold[node_id]

        if feature_idx == -2:
            continue
        
        feature = feature_names[feature_idx]
        value = x_instance[0, feature_idx]


        if feature in categorical_dummy_lookup:
            base_var, active_cat = categorical_dummy_lookup[feature]
            label = var_labels_dutch.get(base_var, base_var)

            all_cats = categorical_vars[base_var][0]
            other_cats = [c for c in all_cats if c != active_cat]

            if value <= threshold:
                rules.append(
                    f"{label} = {' / '.join(other_cats)}"
                )
            else:
                rules.append(
                    f"{label} = {active_cat}"
                )

        elif feature in binary_vars:
            label = var_labels_dutch.get(feature, feature)
            if value <= threshold:
                rules.append(f"{label} = Nee")
            else:
                rules.append(f"{label} = Ja")

        else:
            label = var_labels_dutch.get(feature, feature)
            unit = var_units_dutch.get(feature, "")

            if unit:
                label = f"{label} ({unit})"

            op = "<" if value <= threshold else "≥"

            if unit == "%":
                rounded = round(threshold / 5) * 5
            else:
                rounded = round(threshold, 1)

            rules.append(
                f"{label} {op} {rounded}"
            )

    return rules
