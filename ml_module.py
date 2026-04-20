import streamlit as st
import pandas as pd
import numpy as np
import time
import shap

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import roc_auc_score, root_mean_squared_error
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

def train_models(df, df_numerical, df_categorical, categorical_vars):

    start_time = time.time()
    st.write("### Model Trainen...")

    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=13,
        stratify=df["is_delayed"]
    )

    numerical_cols = [
        c for c in df_numerical.columns
        if c not in {"is_delayed", "delay_pct", "planned_project_duration_days", "delay_days"}
    ]

    feature_df_cols = numerical_cols + list(df_categorical.columns)

    X_train_base = train_df[feature_df_cols].copy()
    X_test_base = test_df[feature_df_cols].copy()

    y_train_classification = train_df["is_delayed"]
    y_test_classification = test_df["is_delayed"]

    train_delayed = train_df[train_df["is_delayed"] == 1].copy()
    test_delayed = test_df[test_df["is_delayed"] == 1].copy()

    y_train_regression = train_delayed["delay_pct"]
    y_test_regression = test_delayed["delay_pct"]

    X_train_regression_base = train_delayed[feature_df_cols].copy()
    X_test_regression_base = test_delayed[feature_df_cols].copy()

    categorical_cols = list(categorical_vars.keys())
    categorical_cols = [
        c for c in categorical_cols
        if c not in {"is_delayed", "delay_pct", "planned_project_duration_days", "delay_days"}
    ]

    X_train_classification = pd.get_dummies(
        X_train_base, columns=categorical_cols, drop_first=True
    )
    X_test_classification = pd.get_dummies(
        X_test_base, columns=categorical_cols, drop_first=True
    )

    X_train_regression = pd.get_dummies(
        X_train_regression_base, columns=categorical_cols, drop_first=True
    )
    X_test_regression = pd.get_dummies(
        X_test_regression_base, columns=categorical_cols, drop_first=True
    )

    X_train_classification, X_test_classification = X_train_classification.align(
        X_test_classification, join="left", axis=1, fill_value=0
    )
    X_train_regression, X_test_regression = X_train_regression.align(
        X_test_regression, join="left", axis=1, fill_value=0
    )

    X_train_classification = X_train_classification.astype(float)
    X_test_classification = X_test_classification.astype(float)
    X_train_regression = X_train_regression.astype(float)
    X_test_regression = X_test_regression.astype(float)

    st.write("Random Forest classifier aan het trainen & tunen...")

    rf_classifier = RandomForestClassifier(
        random_state=13,
        n_jobs=-1
    )

    
    clf_param_grid = {
        "n_estimators": [200],
        "max_depth": [None, 20],
        "min_samples_leaf": [1, 2],
        "max_features": ["sqrt"],
        "class_weight": ["balanced"]
    }

    clf_grid = GridSearchCV(
        rf_classifier,
        clf_param_grid,
        cv=3,
        scoring="roc_auc",
        n_jobs=-1
    )

    clf_grid.fit(X_train_classification, y_train_classification)

    best_classifier = clf_grid.best_estimator_

    y_proba = best_classifier.predict_proba(X_test_classification)[:, 1]
    auc = roc_auc_score(y_test_classification, y_proba)

    st.success(f"Random Forest classifier AUC: {auc:.3f}")
    st.write("Beste parameters:")
    st.json(clf_grid.best_params_)

    st.write("Random Forest regressor aan het trainen & tunen...")

    rf_regressor = RandomForestRegressor(
        random_state=13,
        n_jobs=-1
    )

    reg_param_grid = {
        "n_estimators": [200, 500],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2"]
    }

    reg_grid = GridSearchCV(
        rf_regressor,
        reg_param_grid,
        cv=3,
        scoring="r2",
        n_jobs=-1
    )

    reg_grid.fit(X_train_regression, y_train_regression)

    best_regressor = reg_grid.best_estimator_

    y_pred = best_regressor.predict(X_test_regression)
    rmse = root_mean_squared_error(y_test_regression, y_pred)

    st.success(f"Random Forest regressor RMSE: {rmse:.4f}")
    st.write("Beste parameters:")
    st.json(reg_grid.best_params_)

    st.session_state.shap_explainer_classification = shap.TreeExplainer(best_classifier)
    st.session_state.shap_explainer_regression = shap.TreeExplainer(best_regressor)

    st.info(f"Training voltooid in {time.time() - start_time:.1f} seconden")

    return (
        best_classifier,
        best_regressor,
        X_train_classification,
        y_train_classification,
        X_train_regression,
        y_train_regression,
        X_test_classification,
        X_test_regression,
        test_delayed,
        categorical_vars,
        numerical_cols,
        categorical_cols
    )

def generate_prediction(
    input_data,
    best_classifier,
    best_regressor,
    categorical_vars,
    X_test_classification_columns,
    X_test_regression_columns,
    planned_duration_days
):

    df_num = input_data.select_dtypes(include=[np.number])
    df_cat = input_data.select_dtypes(exclude=[np.number])

    df_cat_encoded = pd.DataFrame()

    for col, choices in categorical_vars.items():
        if isinstance(choices, tuple):
            choices = choices[0]
        for opt in choices:
            df_cat_encoded[f"{col}_{opt}"] = (input_data[col] == opt).astype(int)

    df_final = pd.concat([df_num, df_cat_encoded], axis=1)

    for col in X_test_classification_columns:
        if col not in df_final.columns:
            df_final[col] = 0

    X_input_classification = df_final[X_test_classification_columns]

    for col in X_test_regression_columns:
        if col not in df_final.columns:
            df_final[col] = 0

    X_input_regression = df_final[X_test_regression_columns]

    delay_class = best_classifier.predict(X_input_classification)[0]
    prob_delay = best_classifier.predict_proba(X_input_classification)[:, 1]
    predicted_severity = best_regressor.predict(X_input_regression)

    expected_delay_pct = prob_delay * predicted_severity
    expected_delay_days = expected_delay_pct * planned_duration_days

    return {
        "delay_class": int(delay_class),
        "probability_delay": prob_delay[0],
        "predicted_severity": predicted_severity[0],
        "expected_delay_pct": expected_delay_pct[0],
        "expected_delay_days": expected_delay_days[0]
    }