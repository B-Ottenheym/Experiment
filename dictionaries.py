binary_vars = {
        "project_controls_plan_in_place": 0.70,
        "roles_responsibilities_defined_raci": 0.75,
        "site_logistics_plan_completed": 0.65,
        "quality_management_plan_in_place_qmp": 0.80,
        "change_control_procedure_defined": 0.70,
        "clash_detection_performed_if_bim": 0.85,
        "design_schedule_baseline_approved": 0.70,
        "bim_capability": 0.80,
        "proof_of_financing_submitted": 0.85,
        "payment_security_instrument_included": 0.60,
        "escalation_path_defined": 0.65,
        "land_acquisition_right_of_way_resolved": 0.80,
        "unresolved_utilities_present": 0.25,
        "unresolved_site_access_constraints": 0.25,
        "inspection_test_plan_defined_itp": 0.70,
        "information_management": 0.65,
        "supplier_iso_9001_certified": 0.80,
        "overtime_shift_work_planned": 0.40,
        "collaborative_contracting_bouwteam": 0.25,
        "incentive_mechanisms_included": 0.80,
        "ongoing_legal_disputes": 0.15,
        "project_parties_prior_collaboration": 0.40,
        "weather_contingency_included": 0.55,
        "geotechnical_investigation_completed": 0.80,
        "safety_management_plan_in_place": 0.85,
        "safety_certification_requirement": 0.80,
        "price_escalation_clauses_included": 0.80,
        "traffic_management_plan": 0.60,
        "stakeholder_engagement_plan_in_place": 0.65,
        "benchmarking_against_similar_projects_performed": 0.55
    }

binary_directionality = {
        "project_controls_plan_in_place": -1,
        "roles_responsibilities_defined_raci": -1,
        "site_logistics_plan_completed": -1,
        "quality_management_plan_in_place_qmp": -1,
        "change_control_procedure_defined": -1,
        "clash_detection_performed_if_bim": -1,
        "design_schedule_baseline_approved": -1,
        "bim_capability": -1,
        "proof_of_financing_submitted": -1,
        "payment_security_instrument_included": -1,
        "escalation_path_defined": -1,
        "land_acquisition_right_of_way_resolved": -1,
        "unresolved_utilities_present": +1,
        "unresolved_site_access_constraints": +1,
        "inspection_test_plan_defined_itp": -1,
        "information_management": -1,
        "supplier_iso_9001_certified": -1,
        "overtime_shift_work_planned": +1,
        "collaborative_contracting_bouwteam": -1,
        "incentive_mechanisms_included": -1,
        "ongoing_legal_disputes": +1,
        "project_parties_prior_collaboration": -1,
        "weather_contingency_included": -1,
        "geotechnical_investigation_completed": -1,
        "safety_management_plan_in_place": -1,
        "safety_certification_requirement": -1,
        "price_escalation_clauses_included": -1,
        "traffic_management_plan": -1,
        "stakeholder_engagement_plan_in_place": -1,
        "benchmarking_against_similar_projects_performed": -1
    }

categorical_vars = {
    "approval_responsibility_allocation": (
        ["Opdrachtgever", "Adviseur", "Gezamenlijk"],
        [0.35, 0.40, 0.25]
    ),
    "owner_financial_reliability": (
        ["Laag", "Gemiddeld", "Hoog"],
        [0.20, 0.50, 0.30]
    ),
    "owner_involvement": (
        ["Laag", "Gemiddeld", "Hoog"],
        [0.30, 0.45, 0.25]
    ),
    "change_initiation_rights": (
        ["Opdrachtgever", "Gezamenlijk", "Aannemer"],
        [0.40, 0.40, 0.20]
    ),
    "equipment_ownership": (
        ["Eigen materieel", "Gehuurd", "Combinatie"],
        [0.40, 0.35, 0.25]
    ),
    "site_logistics_complexity": (
        ["Laag", "Gemiddeld", "Hoog"],
        [0.30, 0.45, 0.25]
    ),
    "contract_type": (
        ["UAV 2012", "UAV-GC 2025", "Overig"],
        [0.45, 0.35, 0.20]
    ),
    "authority_involvement_level": (
        ["Lokaal", "Regionaal", "Nationaal"],
        [0.40, 0.40, 0.20]
    ),
    "pricing_mechanism": (
        ["Vast", "Aanpasbaar"],
        [0.55, 0.45]
    ),
    "urban_context": (
        ["Landelijk", "Voorstedelijk", "Dicht stedelijk"],
        [0.25, 0.45, 0.30]
    ),
    "cost_estimate_class_aace_1_5": (
        ["Klasse 1", "Klasse 2", "Klasse 3", "Klasse 4", "Klasse 5"],
        [0.05, 0.15, 0.35, 0.30, 0.15]
    )
}

categorical_mappings = {
    "approval_responsibility_allocation": {
        "Opdrachtgever": 0.5,
        "Adviseur": 0.2,
        "Gezamenlijk": 0.3
    },
    "owner_financial_reliability": {
        "Laag": 0.8,
        "Gemiddeld": 0.5,
        "Hoog": 0.2
    },
    "owner_involvement": {
        "Laag": 0.3,
        "Gemiddeld": 0.5,
        "Hoog": 0.8
    },
    "change_initiation_rights": {
        "Opdrachtgever": 0.8,
        "Gezamenlijk": 0.5,
        "Aannemer": 0.3
    },
    "equipment_ownership": {
        "Eigen materieel": 0.3,
        "Combinatie": 0.5,
        "Gehuurd": 0.8
    },
    "site_logistics_complexity": {
        "Laag": 0.2,
        "Gemiddeld": 0.5,
        "Hoog": 0.8
    },
    "contract_type": {
        "UAV 2012": 0.6,
        "UAV-GC 2025": 0.3,
        "Overig": 0.8
    },
    "authority_involvement_level": {
        "Lokaal": 0.3,
        "Regionaal": 0.5,
        "Nationaal": 0.8
    },
    "pricing_mechanism": {
        "Vast": 0.2,
        "Aanpasbaar": 0.7
    },
    "urban_context": {
        "Landelijk": 0.3,
        "Voorstedelijk": 0.5,
        "Dicht stedelijk": 0.8
    },
    "cost_estimate_class_aace_1_5": {
        "Klasse 1": 0.2,
        "Klasse 2": 0.4,
        "Klasse 3": 0.6,
        "Klasse 4": 0.8,
        "Klasse 5": 1.0
    }
}

continuous_vars = {
    "planned_project_duration_days": (365, 120, 90, 900),
    
    "schedule_level_of_detail_avg_activity_days": (8, 3, 3, 20),

    "scope_definition_completeness_pct": (75, 15, 30, 100),
    "provisional_sums_pct_contract_value": (8, 5, 0, 25),

    "approval_layers_count": (3, 1, 1, 6),

    "percentage_design_complete_at_award_pct": (70, 20, 20, 100),
    "outstanding_design_packages_at_execution_start_count": (2, 2, 0, 8),

    "lead_designer_experience_years": (20, 14, 3, 30),
    "similar_projects_designed_count": (6, 3, 0, 20),
    "design_team_size_fte": (8, 3, 2, 25),

    "financial_prequalification_score_0_100": (70, 15, 30, 100),
    "contract_value_vs_annual_turnover_pct": (45, 20, 10, 150),

    "contractual_payment_terms_days": (30, 10, 7, 90),

    "contractual_decision_time_days": (14, 10, 3, 60),

    "contractor_experience_years": (15, 7, 3, 40),
    "similar_projects_completed_count": (10, 5, 1, 30),
    "technical_tender_score_0_100": (75, 10, 40, 100),

    "method_statement_completeness": (75, 15, 30, 100),
    "share_first_time_methods_pct": (20, 15, 0, 60),

    "subcontracting_share_pct": (45, 25, 10, 80),
    "number_of_subcontractors_count": (6, 3, 1, 20),
    "critical_package_subcontractor_awarded_pre_start_pct": (70, 20, 0, 100),

    "complexity_of_construction_scope_major_packages_wbs_count": (8, 4, 2, 25),

    "meeting_frequency_meetings_per_month_count": (6, 2, 2, 15),
    "number_of_key_stakeholders_count": (8, 4, 2, 25),

    "imported_material_dependency_pct": (30, 15, 0, 80),
    "critical_materials_identified_count": (4, 2, 0, 12),
    "critical_materials_lead_time_gt_8_weeks_count": (2, 1, 0, 8),
    "single_source_critical_materials_count": (1, 1, 0, 5),

    "planned_procurement_lead_time_days": (45, 20, 10, 120),
    "critical_materials_ordered_pre_start_pct": (65, 20, 0, 100),
    "supplier_reliability_pct_on_time_deliveries": (85, 10, 50, 100),

    "equipment_availability_confirmed_pct_critical_equipment": (85, 10, 50, 100),
    "avg_equipment_age_years": (7, 4, 1, 20),

    "avg_operator_experience_years": (8, 4, 1, 25),

    "labour_availability_pct_planned_available_vs_required": (90, 10, 50, 120),
    "dependency_on_scarce_trades_pct": (30, 15, 0, 80),
    "use_of_agency_temporary_labour_pct": (20, 15, 0, 60),
    "critical_trades_confirmed_pct": (75, 20, 0, 100),

    "share_of_certified_workers_pct": (65, 15, 30, 100),
    "planned_onboarding_training_days": (5, 3, 0, 20),
    "avg_experience_of_workforce_years": (9, 4, 2, 30),

    "deviations_from_standard_terms": (2, 1, 0, 10),

    "permits_required_count": (6, 4, 1, 15),
    "permits_obtained_at_start_pct": (80, 45, 0, 100),
    "permit_planned_lead_time_days": (70, 55, 10, 240),

    "historical_weather_affected_days": (20, 10, 5, 60),
    "weather_sensitive_activities_share_pct": (35, 15, 0, 80),

    "contractor_safety_record_trir": (1.5, 0.8, 0.2, 4.0),
    "high_risk_activities_identified_count": (4, 2, 0, 12),
    "safety_training_hours_required": (8, 4, 0, 40),

    "inflation_forecast_pct": (3, 1.5, 0, 10),
    "contract_value_subject_to_indexation_pct": (40, 20, 0, 100),

    "approvals_pending_count": (3, 2, 0, 10),
    "compliance_deliverables_required_count": (5, 3, 0, 20),

    "external_stakeholders_count": (6, 4, 0, 20),
    "outstanding_stakeholder_objections_count": (1, 1, 0, 10),

    "cost_contingency_included_pct": (10, 5, 0, 30)
}

continuous_directionality = {
    "schedule_level_of_detail_avg_activity_days": +1,

    "scope_definition_completeness_pct": -1,
    "provisional_sums_pct_contract_value": +1,

    "approval_layers_count": +1,

    "percentage_design_complete_at_award_pct": -1,
    "outstanding_design_packages_at_execution_start_count": +1,

    "lead_designer_experience_years": -1,
    "similar_projects_designed_count": -1,
    "design_team_size_fte": -1,

    "financial_prequalification_score_0_100": -1,
    "contract_value_vs_annual_turnover_pct": +1,

    "contractual_payment_terms_days": +1,

    "contractual_decision_time_days": +1,

    "contractor_experience_years": -1,
    "similar_projects_completed_count": -1,
    "technical_tender_score_0_100": -1,

    "method_statement_completeness": -1,
    "share_first_time_methods_pct": +1,

    "subcontracting_share_pct": +1,
    "number_of_subcontractors_count": +1,
    "critical_package_subcontractor_awarded_pre_start_pct": -1,

    "complexity_of_construction_scope_major_packages_wbs_count": +1,

    "meeting_frequency_meetings_per_month_count": -1,
    "number_of_key_stakeholders_count": +1,

    "imported_material_dependency_pct": +1,
    "critical_materials_identified_count": +1,
    "critical_materials_lead_time_gt_8_weeks_count": +1,
    "single_source_critical_materials_count": +1,

    "planned_procurement_lead_time_days": +1,
    "critical_materials_ordered_pre_start_pct": -1,
    "supplier_reliability_pct_on_time_deliveries": -1,

    "equipment_availability_confirmed_pct_critical_equipment": -1,
    "avg_equipment_age_years": +1,

    "avg_operator_experience_years": -1,

    "labour_availability_pct_planned_available_vs_required": -1,
    "dependency_on_scarce_trades_pct": +1,
    "use_of_agency_temporary_labour_pct": +1,
    "critical_trades_confirmed_pct": -1,

    "share_of_certified_workers_pct": -1,
    "planned_onboarding_training_days": -1,
    "avg_experience_of_workforce_years": -1,

    "deviations_from_standard_terms": +1,

    "permits_required_count": +1,
    "permits_obtained_at_start_pct": -1,
    "permit_planned_lead_time_days": +1,

    "historical_weather_affected_days": +1,
    "weather_sensitive_activities_share_pct": +1,

    "contractor_safety_record_trir": +1,
    "high_risk_activities_identified_count": +1,
    "safety_training_hours_required": -1,

    "inflation_forecast_pct": +1,
    "contract_value_subject_to_indexation_pct": +1,

    "approvals_pending_count": +1,
    "compliance_deliverables_required_count": +1,

    "external_stakeholders_count": +1,
    "outstanding_stakeholder_objections_count": +1,

    "cost_contingency_included_pct": -1
}

integer_continuous_vars = {
    # Planning & schedule
    "planned_project_duration_days",
    "schedule_level_of_detail_avg_activity_days",
    "approval_layers_count",
    "outstanding_design_packages_at_execution_start_count",

    # Design / team
    "lead_designer_experience_years",
    "similar_projects_designed_count",
    "design_team_size_fte",

    # Payments / governance
    "contractual_payment_terms_days",
    "contractual_decision_time_days",

    # Contractor
    "contractor_experience_years",
    "similar_projects_completed_count",

    # Subcontracting / complexity
    "number_of_subcontractors_count",
    "complexity_of_construction_scope_major_packages_wbs_count",

    # Communication
    "meeting_frequency_meetings_per_month_count",
    "number_of_key_stakeholders_count",

    # Materials
    "critical_materials_identified_count",
    "critical_materials_lead_time_gt_8_weeks_count",
    "single_source_critical_materials_count",
    "planned_procurement_lead_time_days",

    # Equipment / labour
    "avg_equipment_age_years",
    "avg_operator_experience_years",
    "planned_onboarding_training_days",
    "avg_experience_of_workforce_years",

    # Permits / external
    "deviations_from_standard_terms",
    "permits_required_count",
    "permit_planned_lead_time_days",
    "historical_weather_affected_days",
    "high_risk_activities_identified_count",
    "safety_training_hours_required",

    # Compliance / stakeholders
    "approvals_pending_count",
    "compliance_deliverables_required_count",
    "external_stakeholders_count",
    "outstanding_stakeholder_objections_count",
}

var_groups = {
    "planning_control": [
        "schedule_level_of_detail_avg_activity_days",          # 1.1
        "project_controls_plan_in_place",                      # 2.1
        "roles_responsibilities_defined_raci",                 # 2.2
        "site_logistics_plan_completed",                       # 2.3
        "quality_management_plan_in_place_qmp",                # 2.4
        "design_schedule_baseline_approved",                   # 6.1
        "percentage_design_complete_at_award_pct",             # 6.2
        "outstanding_design_packages_at_execution_start_count",# 6.3
        "meeting_frequency_meetings_per_month_count",          # 17.1
        "information_management",                              # 17.2
        "number_of_key_stakeholders_count",                    # 17.3
        "cost_estimate_class_aace_1_5",                        # 35.1
        "cost_contingency_included_pct",                       # 35.2
        "benchmarking_against_similar_projects_performed"      # 35.3
    ],
    "design_readiness_quality": [
        "clash_detection_performed_if_bim",                    # 5.1
        "lead_designer_experience_years",                      # 7.1
        "similar_projects_designed_count",                     # 7.2
        "design_team_size_fte",                                # 7.3
        "bim_capability",                                      # 7.4
        "approval_layers_count",                               # 4.1
        "approval_responsibility_allocation"                   # 4.2
    ],
    "scope_change_management": [
        "scope_definition_completeness_pct",                   # 3.1
        "provisional_sums_pct_contract_value",                 # 3.2
        "change_control_procedure_defined",                    # 3.3
        "owner_involvement",                                   # 11.1
        "change_initiation_rights"                             # 11.2
    ],
    "owner_governance": [
        "contractual_payment_terms_days",                      # 9.1
        "payment_security_instrument_included",                # 9.2
        "owner_financial_reliability",                         # 9.3
        "contractual_decision_time_days",                      # 10.1
        "escalation_path_defined",                             # 10.2
        "ongoing_legal_disputes",                               # 27.1
        "project_parties_prior_collaboration"                  # 27.2
    ],
    "contract_commercial_structure": [
        "contract_type",                                       # 26.1
        "collaborative_contracting_bouwteam",                  # 26.2
        "incentive_mechanisms_included",                       # 26.3
        "deviations_from_standard_terms",                      # 26.4 
        "inflation_forecast_pct",                              # 32.1
        "price_escalation_clauses_included",                   # 32.2
        "pricing_mechanism",                                   # 32.3
        "contract_value_subject_to_indexation_pct"             # 32.4
    ],
    "contractor_supply_chain_capability": [
        "financial_prequalification_score_0_100",              # 8.1
        "contract_value_vs_annual_turnover_pct",               # 8.2
        "proof_of_financing_submitted",                        # 8.3
        "contractor_experience_years",                         # 13.1
        "similar_projects_completed_count",                    # 13.2
        "technical_tender_score_0_100",                        # 13.3
        "method_statement_completeness",                        #14.1
        "share_first_time_methods_pct",                         # 14.2
        "subcontracting_share_pct",                            # 15.1
        "number_of_subcontractors_count",                      # 15.2
        "critical_package_subcontractor_awarded_pre_start_pct",# 15.3
        "imported_material_dependency_pct",                    # 18.1
        "critical_materials_identified_count",                 # 18.2
        "critical_materials_lead_time_gt_8_weeks_count",       # 18.3
        "single_source_critical_materials_count",              # 18.4
        "planned_procurement_lead_time_days",                  # 19.1
        "critical_materials_ordered_pre_start_pct",            # 19.2
        "supplier_reliability_pct_on_time_deliveries",         # 19.3
        "supplier_iso_9001_certified",                         # 20.1
        "equipment_availability_confirmed_pct_critical_equipment", # 21.1
        "equipment_ownership",                                 # 21.2
        "avg_equipment_age_years",                              # 21.3
        "avg_operator_experience_years"                        # 22.1
    ],
    "labour_productivity": [
        "labour_availability_pct_planned_available_vs_required", # 23.1
        "dependency_on_scarce_trades_pct",                       # 23.2
        "use_of_agency_temporary_labour_pct",                    # 23.3
        "critical_trades_confirmed_pct",                         # 23.4
        "overtime_shift_work_planned",                           # 24.1
        "site_logistics_complexity",                             # 24.2
        "share_of_certified_workers_pct",                        # 25.1
        "planned_onboarding_training_days",                      # 25.2
        "avg_experience_of_workforce_years"                      # 25.3
    ],
    "site_external_conditions": [
        "land_acquisition_right_of_way_resolved",                # 12.1
        "unresolved_utilities_present",                          # 12.2
        "unresolved_site_access_constraints",                    # 12.3
        "permits_required_count",                                # 28.1
        "permits_obtained_at_start_pct",                         # 28.2
        "authority_involvement_level",                            # 28.3
        "permit_planned_lead_time_days",                         # 28.4
        "historical_weather_affected_days",                      # 29.1
        "weather_contingency_included",                          # 29.2
        "weather_sensitive_activities_share_pct",                # 29.3
        "geotechnical_investigation_completed",                  # 30.1
        "approvals_pending_count",                               # 33.1
        "compliance_deliverables_required_count",                # 33.2
        "urban_context",                                         # 34.1
        "external_stakeholders_count",                           # 34.2
        "outstanding_stakeholder_objections_count",              # 34.3
        "traffic_management_plan",                               # 34.4
        "stakeholder_engagement_plan_in_place"                   # 34.5
    ],
    "safety_rework": [
        "inspection_test_plan_defined_itp",                      # 16.1
        "complexity_of_construction_scope_major_packages_wbs_count", # 16.2
        "contractor_safety_record_trir",                         # 31.1
        "safety_management_plan_in_place",                       # 31.2
        "safety_certification_requirement",                      # 31.3
        "high_risk_activities_identified_count",                 # 31.4
        "safety_training_hours_required"                         # 31.5
    ],
    "context": ["planned_project_duration_days"]
}

group_weights = {
    "planning_control": 0.16,
    "design_readiness_quality": 0.16,
    "scope_change_management": 0.07,
    "owner_governance": 0.14,
    "contract_commercial_structure": 0.07,
    "contractor_supply_chain_capability": 0.11,
    "labour_productivity": 0.10,
    "site_external_conditions": 0.14,
    "safety_rework": 0.05
}

inter_group_effects = {
    "scope_change_management": {
        "design_readiness_quality": 0.30,
        "owner_governance": 0.30
    },
    "safety_rework": {
        "design_readiness_quality": 0.25,
        "labour_productivity": 0.20
    },
    "planning_control": {
        "owner_governance": 0.20,
        "site_external_conditions": 0.20
    },
    "owner_governance": {
        "contract_commercial_structure": 0.15
    },
    "contractor_supply_chain_capability": {
        "contract_commercial_structure": 0.20,
        "planning_control": 0.25,
        "site_external_conditions": 0.25
    },
    "labour_productivity": {
        "planning_control": 0.20,
        "contractor_supply_chain_capability": 0.20
    }
}

within_group_loadings = {
    "schedule_level_of_detail_avg_activity_days": 0.8,              # 1.1
    "project_controls_plan_in_place": 0.6,                          # 2.1
    "roles_responsibilities_defined_raci": 0.6,                     # 2.2
    "site_logistics_plan_completed": 0.6,                           # 2.3
    "quality_management_plan_in_place_qmp": 0.6,                    # 2.4
    "design_schedule_baseline_approved": 0.4,                       # 6.1
    "percentage_design_complete_at_award_pct": 1.0,                 # 6.2
    "outstanding_design_packages_at_execution_start_count": 1.0,    # 6.3
    "meeting_frequency_meetings_per_month_count": 0.6,              # 17.1
    "information_management": 0.8,                                  # 17.2
    "number_of_key_stakeholders_count": 0.6,                        # 17.3
    "cost_estimate_class_aace_1_5": 0.8,                            # 35.1
    "cost_contingency_included_pct": 0.6,                           # 35.2
    "benchmarking_against_similar_projects_performed": 0.4,         # 35.3

    "clash_detection_performed_if_bim": 0.4,                        # 5.1
    "lead_designer_experience_years": 0.4,                          # 7.1
    "similar_projects_designed_count": 0.4,                         # 7.2
    "design_team_size_fte": 0.4,                                    # 7.3
    "bim_capability": 0.4,                                          # 7.4
    "approval_layers_count": 0.8,                                   # 4.1
    "approval_responsibility_allocation": 0.4,                      # 4.2

    "scope_definition_completeness_pct": 0.6,                       # 3.1
    "provisional_sums_pct_contract_value": 0.6,                     # 3.2
    "change_control_procedure_defined": 0.6,                        # 3.3
    "owner_involvement": 0.6,                                       # 11.1
    "change_initiation_rights": 0.6,                                # 11.3

    "contractual_payment_terms_days": 0.6,                          # 9.1
    "payment_security_instrument_included": 0.4,                    # 9.2
    "owner_financial_reliability": 0.8,                             # 9.3
    "contractual_decision_time_days": 0.8,                          # 10.1
    "escalation_path_defined": 0.4,                                 # 10.2
    "ongoing_legal_disputes": 1,                                    # 27.1
    "project_parties_prior_collaboration": 0.4,                     # 27.2

    "contract_type": 1,                                             # 26.1
    "collaborative_contracting_bouwteam": 0.4,                      # 26.2
    "incentive_mechanisms_included": 0.4,                           # 26.3
    "deviations_from_standard_terms": 0.6,                          # 26.4 
    "inflation_forecast_pct": 0.6,                                  # 32.1
    "price_escalation_clauses_included": 0.4,                       # 32.2
    "pricing_mechanism": 0.4,                                       # 32.3
    "contract_value_subject_to_indexation_pct": 0.4,                # 32.4

    "financial_prequalification_score_0_100": 0.8,                  # 8.1
    "contract_value_vs_annual_turnover_pct": 0.6,                   # 8.2
    "proof_of_financing_submitted": 0.4,                            # 8.3
    "contractor_experience_years": 0.8,                             # 13.1
    "similar_projects_completed_count": 0.6,                        # 13.2
    "technical_tender_score_0_100": 0.6,                            # 13.3
    "method_statement_completeness": 0.6,                           # 14.1
    "share_first_time_methods_pct": 0.4,                            # 14.2
    "subcontracting_share_pct": 0.6,                                # 15.1
    "number_of_subcontractors_count": 0.4,                          # 15.2
    "critical_package_subcontractor_awarded_pre_start_pct": 0.6,    # 15.3
    "imported_material_dependency_pct": 0.4,                        # 18.1
    "critical_materials_identified_count": 0.4,                     # 18.2
    "critical_materials_lead_time_gt_8_weeks_count": 0.8,           # 18.3
    "single_source_critical_materials_count": 0.6,                  # 18.4
    "planned_procurement_lead_time_days": 0.6,                      # 19.1
    "critical_materials_ordered_pre_start_pct": 0.6,                # 19.2
    "supplier_reliability_pct_on_time_deliveries": 0.8,             # 19.3    
    "supplier_iso_9001_certified": 0.4,                             # 20.1
    "equipment_availability_confirmed_pct_critical_equipment": 0.6, # 21.1
    "equipment_ownership": 0.4,                                     # 21.2
    "avg_equipment_age_years": 0.4,                                 # 21.3
    "avg_operator_experience_years": 0.4,                           # 22.1

    "labour_availability_pct_planned_available_vs_required": 0.8,   # 23.1
    "dependency_on_scarce_trades_pct": 0.6,                         # 23.2
    "use_of_agency_temporary_labour_pct": 0.4,                      # 23.3
    "critical_trades_confirmed_pct": 0.6,                           # 23.4
    "overtime_shift_work_planned": 0.6,                             # 24.1
    "site_logistics_complexity": 0.4,                               # 24.2
    "share_of_certified_workers_pct": 0.6,                          # 25.1
    "planned_onboarding_training_days": 0.4,                        # 25.2
    "avg_experience_of_workforce_years": 0.8,                       # 25.3

    "land_acquisition_right_of_way_resolved": 0.6,                  # 12.1
    "unresolved_utilities_present": 0.6,                            # 12.2
    "unresolved_site_access_constraints": 0.6,                      # 12.3
    "permits_required_count": 0.6,                                  # 28.1
    "permits_obtained_at_start_pct": 1,                             # 28.2
    "authority_involvement_level": 0.4,                             # 28.3
    "permit_planned_lead_time_days": 0.8,                           # 28.4
    "historical_weather_affected_days": 0.6,                        # 29.1
    "weather_contingency_included": 0.4,                            # 29.2
    "weather_sensitive_activities_share_pct": 1  ,                  # 29.3
    "geotechnical_investigation_completed": 0.6,                    # 30.1
    "approvals_pending_count": 0.6,                                 # 33.1
    "compliance_deliverables_required_count": 0.4,                  # 33.2
    "urban_context": 1,                                             # 34.1
    "external_stakeholders_count": 0.4,                             # 34.2
    "outstanding_stakeholder_objections_count": 0.8,                # 34.3
    "traffic_management_plan": 0.4,                                 # 34.4
    "stakeholder_engagement_plan_in_place": 0.4,                    # 34.5

    "inspection_test_plan_defined_itp": 0.6,                        # 16.1
    "complexity_of_construction_scope_major_packages_wbs_count": 0.6, # 16.2
    "contractor_safety_record_trir": 0.8,                           # 31.1
    "safety_management_plan_in_place": 0.6,                         # 31.2
    "safety_certification_requirement": 0.4,                        # 31.3
    "high_risk_activities_identified_count": 0.4,                   # 31.4
    "safety_training_hours_required": 0.4                           # 31.5
}

var_labels_dutch = {
    "planned_project_duration_days": "Geplande projectduur (dagen)",
    "is_delayed": "Vertraagd",
    "delay_pct": "Vertraging (%)",
    "delay_days": "Vertraging (dagen)",

    "schedule_level_of_detail_avg_activity_days": "Detailniveau planning",
    "project_controls_plan_in_place": "Project Controls Plan (PCP) aanwezig",
    "roles_responsibilities_defined_raci": "Rollen en verantwoordelijkheden vastgelegd (RACI)",
    "site_logistics_plan_completed": "Bouwplaatslogistiek plan afgerond",
    "quality_management_plan_in_place_qmp": "Kwaliteitsmanagementplan aanwezig",
    "design_schedule_baseline_approved": "Ontwerpplanning goedgekeurd",
    "percentage_design_complete_at_award_pct": "Ontwerpgereedheid bij contractverlening",
    "outstanding_design_packages_at_execution_start_count": "Openstaande ontwerppakketten",
    "meeting_frequency_meetings_per_month_count": "Vergaderfrequentie",
    "information_management": "Informatiemanagement volgens ISO 19650",
    "number_of_key_stakeholders_count": "Aantal kernstakeholders",
    "cost_estimate_class_aace_1_5": "Kostenramingsklasse (AACE)",
    "cost_contingency_included_pct": "Kostencontingentie opgenomen",
    "benchmarking_against_similar_projects_performed": "Benchmarking met vergelijkbare projecten uitgevoerd",

    "clash_detection_performed_if_bim": "Clashdetectie uitgevoerd (BIM)",
    "lead_designer_experience_years": "Ervaring hoofdontwerper",
    "similar_projects_designed_count": "Aantal vergelijkbare projecten ontworpen",
    "design_team_size_fte": "Omvang ontwerpteam (fte)",
    "bim_capability": "BIM-capaciteit",
    "approval_layers_count": "Aantal goedkeuringslagen",
    "approval_responsibility_allocation": "Verantwoordelijkheid goedkeuring",

    "scope_definition_completeness_pct": "Volledigheid scope-definitie",
    "provisional_sums_pct_contract_value": "Stelposten",
    "change_control_procedure_defined": "Wijzigingsprocedure vastgelegd",
    "owner_involvement": "Betrokkenheid opdrachtgever",
    "change_initiation_rights": "Wijzigingsinitiatief vastgesteld",

    "contractual_payment_terms_days": "Betalingstermijn contract",
    "payment_security_instrument_included": "Betalingszekerheid contractueel opgenomen",
    "owner_financial_reliability": "Financiële betrouwbaarheid opdrachtgever",
    "contractual_decision_time_days": "Contractuele beslistermijn",
    "escalation_path_defined": "Escalatieprocedure vastgelegd",
    "ongoing_legal_disputes": "Lopende juridische geschillen",
    "project_parties_prior_collaboration": "Eerdere samenwerking projectpartijen",

    "contract_type": "Contractvorm",
    "collaborative_contracting_bouwteam": "Bouwteam",
    "incentive_mechanisms_included": "Incentivemechanismen opgenomen",
    "deviations_from_standard_terms": "Afwijkingen van standaardvoorwaarden",
    "inflation_forecast_pct": "Inflatieverwachting",
    "price_escalation_clauses_included": "Prijsescalatieclausules opgenomen",
    "pricing_mechanism": "Prijsmechanisme",
    "contract_value_subject_to_indexation_pct": "Contractwaarde onder indexering",

    "financial_prequalification_score_0_100": "Financiële prekwalificatiescore",
    "contract_value_vs_annual_turnover_pct": "Contractwaarde t.o.v. jaaromzet",
    "proof_of_financing_submitted": "Financieringsbewijs aangeleverd",
    "contractor_experience_years": "Ervaring aannemer",
    "similar_projects_completed_count": "Aantal vergelijkbare projecten voltooid door aannemer",
    "technical_tender_score_0_100": "Kwaliteitsscore BPKV",
    "method_statement_completeness": "Volledigheid werkinstructies",
    "share_first_time_methods_pct": "Aandeel nieuwe uitvoeringsmethoden",
    "subcontracting_share_pct": "Uitbestedingsaandeel",
    "number_of_subcontractors_count": "Aantal onderaannemers",
    "critical_package_subcontractor_awarded_pre_start_pct": "Kritische pakketten vooraf gegund",

    "imported_material_dependency_pct": "Afhankelijkheid geïmporteerde materialen",
    "critical_materials_identified_count": "Aantal kritische materialen",
    "critical_materials_lead_time_gt_8_weeks_count": "Kritische materialen met levertijd > 8 weken",
    "single_source_critical_materials_count": "Kritische materialen met één leverancier",
    "planned_procurement_lead_time_days": "Geplande inkoopdoorlooptijd",
    "critical_materials_ordered_pre_start_pct": "Kritische materialen vooraf besteld",
    "supplier_reliability_pct_on_time_deliveries": "Leverbetrouwbaarheid leveranciers",
    "supplier_iso_9001_certified": "Leveranciers ISO 9001-gecertificeerd",
    "equipment_availability_confirmed_pct_critical_equipment": "Beschikbaarheid materieel bevestigd",
    "equipment_ownership": "Eigendom materieel",
    "avg_equipment_age_years": "Gemiddelde leeftijd materieel",
    "avg_operator_experience_years": "Gemiddelde ervaring machinisten",

    "labour_availability_pct_planned_available_vs_required": "Beschikbaarheid arbeid",
    "dependency_on_scarce_trades_pct": "Afhankelijkheid schaarse vakgebieden",
    "use_of_agency_temporary_labour_pct": "Inzet uitzend-/tijdelijk personeel",
    "critical_trades_confirmed_pct": "Kritische vakgebieden bevestigd",
    "overtime_shift_work_planned": "Overwerk / ploegendienst gepland",
    "site_logistics_complexity": "Complexiteit bouwplaatslogistiek",
    "share_of_certified_workers_pct": "Aandeel gecertificeerde medewerkers",
    "planned_onboarding_training_days": "Geplande inwerk- en trainingsdagen",
    "avg_experience_of_workforce_years": "Gemiddelde ervaring personeel",

    "land_acquisition_right_of_way_resolved": "Grondverwerving afgerond",
    "unresolved_utilities_present": "Onopgeloste kabels en leidingen",
    "unresolved_site_access_constraints": "Onopgeloste bereikbaarheid",
    "permits_required_count": "Aantal vereiste vergunningen",
    "permits_obtained_at_start_pct": "Vergunningen reeds verkregen",
    "authority_involvement_level": "Niveau betrokken overheid",
    "permit_planned_lead_time_days": "Geplande vergunningdoorlooptijd",
    "historical_weather_affected_days": "Historisch weergevoelige dagen",
    "weather_contingency_included": "Weercontingentie opgenomen",
    "weather_sensitive_activities_share_pct": "Aandeel weergevoelige activiteiten",
    "geotechnical_investigation_completed": "Geotechnisch onderzoek uitgevoerd",
    "approvals_pending_count": "Nog openstaande goedkeuringen",
    "compliance_deliverables_required_count": "Compliance-documenten vereist",
    "urban_context": "Stedelijke context",
    "external_stakeholders_count": "Aantal externe stakeholders",
    "outstanding_stakeholder_objections_count": "Openstaande bezwaren stakeholders",
    "traffic_management_plan": "Verkeersmanagementplan aanwezig",
    "stakeholder_engagement_plan_in_place": "Stakeholdermanagementplan aanwezig",

    "inspection_test_plan_defined_itp": "Inspectie- en testplan vastgesteld",
    "complexity_of_construction_scope_major_packages_wbs_count": "Complexiteit uitvoeringsscope",
    "contractor_safety_record_trir": "Veiligheidsscore aannemer (TRIR)",
    "safety_management_plan_in_place": "Veiligheidsmanagementplan aanwezig",
    "safety_certification_requirement": "VCA-certificering vereist",
    "high_risk_activities_identified_count": "Hoog-risicoactiviteiten geïdentificeerd",
    "safety_training_hours_required": "Vereiste veiligheidsopleidingsuren"
}

var_descriptions_dutch = {

    # Cause 1
    "schedule_level_of_detail_avg_activity_days":
        "Gemiddelde geplande activiteitsduur in de basisplanning, gebruikt als maat voor het detailniveau van de planning.",

    # Cause 2
    "project_controls_plan_in_place":
        "Geeft aan of vóór start uitvoering een gedocumenteerd projectbeheersplan aanwezig is waarin monitoring-, rapportage- en beheersprocedures zijn vastgelegd.",

    "roles_responsibilities_defined_raci":
        "Geeft aan of vóór start uitvoering een formele verantwoordelijkhedenmatrix (RACI) is opgesteld waarin rollen en beslissingsbevoegdheden zijn vastgelegd.",

    "site_logistics_plan_completed":
        "Geeft aan of vóór start uitvoering een gedocumenteerd bouwplaatslogistiek plan is opgesteld.",

    "quality_management_plan_in_place_qmp":
        "Geeft aan of vóór start uitvoering een formeel kwaliteitsmanagementplan is vastgesteld.",

    # Cause 3
    "scope_definition_completeness_pct":
        "Percentage van de WBS-elementen waarvoor scope, hoeveelheden en specificaties zijn vastgelegd bij start uitvoering.",

    "provisional_sums_pct_contract_value":
        "Aandeel van de totale contractwaarde dat is toegewezen aan provisionele posten, uitgedrukt als percentage.",

    "change_control_procedure_defined":
        "Geeft aan of vóór start uitvoering een formele procedure is vastgelegd voor het identificeren, beoordelen en goedkeuren van scopewijzigingen.",

    # Cause 4
    "approval_layers_count":
        "Aantal formele goedkeuringsstappen dat vereist is voor ontwerpdocumenten, werktekeningen of wijzigingen.",

    "approval_responsibility_allocation":
        "Contractueel verantwoordelijke partij voor goedkeuringen, geclassificeerd als opdrachtgever, adviseur of gezamenlijke verantwoordelijkheid.",

    # Cause 5
    "clash_detection_performed_if_bim":
        "Geeft aan of vóór start uitvoering clashdetectie of modelcoördinatie is uitgevoerd (indien BIM wordt toegepast).",

    # Cause 6
    "design_schedule_baseline_approved":
        "Geeft aan of vóór start uitvoering een basisplanning voor ontwerpoplveringen formeel is goedgekeurd.",

    "percentage_design_complete_at_award_pct":
        "Percentage van de totale ontwerpomvang dat gereed is op het moment van contractverlening.",

    "outstanding_design_packages_at_execution_start_count":
        "Aantal ontwerppakketten dat bij start uitvoering nog niet is afgerond.",

    # Cause 7
    "lead_designer_experience_years":
        "Aantal jaren relevante professionele ervaring van de hoofdontwerper die aan het project is toegewezen.",

    "similar_projects_designed_count":
        "Aantal vergelijkbare projecten dat eerder door het ontwerpteam is ontworpen.",

    "design_team_size_fte":
        "Aantal fulltime-equivalent ontwerpers dat bij start uitvoering aan het project is toegewezen.",

    "bim_capability":
        "Geeft aan of het ontwerpteam beschikt over interne BIM-capaciteit voor coördinatie en modelgebaseerd ontwerpen.",

    # Cause 8
    "financial_prequalification_score_0_100":
        "Score die de financiële draagkracht van de aannemer weerspiegelt op basis van formele prekwalificatieprocedures.",

    "contract_value_vs_annual_turnover_pct":
        "Verhouding tussen de contractwaarde en de jaarlijkse omzet van de aannemer, uitgedrukt als percentage.",

    "proof_of_financing_submitted":
        "Geeft aan of vóór start uitvoering formeel bewijs van zekergestelde financiering is aangeleverd.",

    # Cause 9
    "contractual_payment_terms_days":
        "Aantal kalenderdagen tussen facturatie en de contractuele betalingstermijn.",

    "payment_security_instrument_included":
        "Geeft aan of betalingszekerheden (zoals bankgaranties) contractueel zijn opgenomen.",

    "owner_financial_reliability":
        "Classificatie van de financiële betrouwbaarheid van de opdrachtgever als laag, middel of hoog op basis van organisatorische kenmerken.",

    # Cause 10
    "contractual_decision_time_days":
        "Maximaal aantal kalenderdagen dat contractueel is toegestaan voor besluitvorming.",

    "escalation_path_defined":
        "Geeft aan of een formeel escalatiemechanisme voor onopgeloste besluiten is vastgelegd.",

    # Cause 11
    "owner_involvement":
        "Verwacht niveau van betrokkenheid van de opdrachtgever tijdens de uitvoering, geclassificeerd als laag, middel of hoog.",

    "change_initiation_rights":
        "Verdeling van het recht om wijzigingen te initiëren, geclassificeerd als opdrachtgever, gezamenlijk of aannemer.",

    # Cause 12
    "land_acquisition_right_of_way_resolved":
        "Geeft aan of grondverwerving en rechten van overpad vóór start uitvoering zijn opgelost.",

    "unresolved_utilities_present":
        "Geeft aan of bij start uitvoering nog onopgeloste verleggingen van kabels en leidingen aanwezig zijn.",

    "unresolved_site_access_constraints":
        "Geeft aan of bij start uitvoering nog onopgeloste beperkingen in de bereikbaarheid van de bouwplaats bestaan.",

    # Cause 13
    "contractor_experience_years":
        "Aantal jaren relevante professionele ervaring van de hoofdaannemer.",

    "similar_projects_completed_count":
        "Aantal vergelijkbare projecten dat eerder door de aannemer is gerealiseerd.",

    "technical_tender_score_0_100":
        "Score die de technische kwaliteit van de inschrijvingsdocumenten van de aannemer weerspiegelt.",

    # Cause 14
    "method_statement_completeness":
        "Percentage van de bouwactiviteiten waarvoor goedgekeurde werkinstructies beschikbaar zijn bij start uitvoering.",

    "share_first_time_methods_pct":
        "Percentage van de projectscope dat gepland is om te worden uitgevoerd met methoden die de aannemer niet eerder heeft toegepast.",

    # Cause 15
    "subcontracting_share_pct":
        "Percentage van de totale projectscope dat wordt uitbesteed aan onderaannemers.",

    "number_of_subcontractors_count":
        "Totaal aantal onderaannemers dat bij het project betrokken is.",

    "critical_package_subcontractor_awarded_pre_start_pct":
        "Percentage van kritische onderaannemingspakketten dat vóór start uitvoering is gegund.",

    # Cause 16
    "inspection_test_plan_defined_itp":
        "Geeft aan of vóór start uitvoering een formeel inspectie- en testplan (ITP) is vastgesteld.",

    "complexity_of_construction_scope_major_packages_wbs_count":
        "Aantal grote uitvoeringspakketten of hoog-niveau WBS-elementen dat de uitvoeringsscope vormt.",

    # Cause 17
    "meeting_frequency_meetings_per_month_count":
        "Aantal formele coördinatievergaderingen dat per maand tijdens de uitvoering is gepland.",

    "information_management":
        "Geeft aan of informatiemanagement wordt uitgevoerd in overeenstemming met ISO 19650.",

    "number_of_key_stakeholders_count":
        "Aantal interne en externe stakeholders dat betrokken is bij de projectuitvoering.",

    # Cause 18
    "imported_material_dependency_pct":
        "Percentage van kritische materialen dat internationaal wordt ingekocht.",

    "critical_materials_identified_count":
        "Aantal materialen dat als kritisch voor de projectuitvoering is aangemerkt.",

    "critical_materials_lead_time_gt_8_weeks_count":
        "Aantal kritische materialen met een geplande levertijd van meer dan acht weken.",

    "single_source_critical_materials_count":
        "Aantal kritische materialen dat van slechts één leverancier wordt betrokken.",

    # Cause 19
    "planned_procurement_lead_time_days":
        "Geplande tijd tussen bestelling en levering van kritische materialen, uitgedrukt in dagen.",

    "critical_materials_ordered_pre_start_pct":
        "Percentage van kritische materialen dat vóór start uitvoering is besteld.",

    "supplier_reliability_pct_on_time_deliveries":
        "Percentage historische leveringen dat door geselecteerde leveranciers op tijd is uitgevoerd.",

    # Cause 20
    "supplier_iso_9001_certified":
        "Geeft aan of leveranciers van kritische materialen beschikken over een ISO 9001-certificering.",

    # Cause 21
    "equipment_availability_confirmed_pct_critical_equipment":
        "Percentage van vereist kritisch materieel waarvan de beschikbaarheid bij start uitvoering is bevestigd.",

    "equipment_ownership":
        "Eigendomsvorm van kritisch materieel, geclassificeerd als eigendom, gehuurd of gemengd.",

    "avg_equipment_age_years":
        "Gemiddelde leeftijd van kritisch materieel, uitgedrukt in jaren.",

    # Cause 22
    "avg_operator_experience_years":
        "Gemiddeld aantal jaren ervaring van materieeloperators dat aan het project is toegewezen.",

    # Cause 23
    "labour_availability_pct_planned_available_vs_required":
        "Percentage beschikbare arbeidskrachten ten opzichte van de geplande arbeidsbehoefte.",

    "dependency_on_scarce_trades_pct":
        "Percentage van de totale arbeidsuren dat betrekking heeft op als schaars aangemerkte vakgebieden.",

    "use_of_agency_temporary_labour_pct":
        "Percentage van de totale arbeidsuren dat gepland is te worden ingevuld door uitzend- of tijdelijk personeel.",

    "critical_trades_confirmed_pct":
        "Percentage kritische vakgebieden dat contractueel is bevestigd vóór start uitvoering.",

    # Cause 24
    "overtime_shift_work_planned":
        "Geeft aan of tijdens de uitvoering overwerk of ploegendienst is gepland.",

    "site_logistics_complexity":
        "Classificatie van de complexiteit van de bouwplaatslogistiek als laag, middel of hoog op basis van bereikbaarheid, ruimte en operationele beperkingen.",

    # Cause 25
    "share_of_certified_workers_pct":
        "Percentage van het personeel dat beschikt over vereiste professionele of veiligheidsgerelateerde certificeringen.",

    "planned_onboarding_training_days":
        "Aantal dagen dat is gereserveerd voor inwerk- of trainingsactiviteiten vóór of tijdens de uitvoering.",

    "avg_experience_of_workforce_years":
        "Gemiddeld aantal jaren relevante werkervaring van het projectpersoneel.",

    # Cause 26
    "contract_type":
        "Primaire contractvorm die van toepassing is op het project, zoals UAV 2012, UAV-GC 2025 of een alternatieve vorm.",

    "collaborative_contracting_bouwteam":
        "Geeft aan of een samenwerkingsgerichte contractvorm of bouwteamconstructie wordt toegepast.",

    "incentive_mechanisms_included":
        "Geeft aan of contractuele stimuleringsmechanismen zijn opgenomen.",

    "deviations_from_standard_terms":
        "Aantal afwijkingen van standaard contractvoorwaarden dat in het contract is opgenomen.",

    # Cause 27
    "ongoing_legal_disputes":
        "Geeft aan of bij start uitvoering lopende juridische geschillen tussen projectpartijen bestaan.",

    "project_parties_prior_collaboration":
        "Geeft aan of belangrijke projectpartijen eerder op andere projecten hebben samengewerkt.",

    # Cause 28
    "permits_required_count":
        "Aantal vergunningen dat vereist is voor de uitvoering van het project.",

    "permits_obtained_at_start_pct":
        "Percentage van de vereiste vergunningen dat bij start uitvoering is verkregen.",

    "authority_involvement_level":
        "Hoogst betrokken overheidsniveau bij vergunningverlening, geclassificeerd als lokaal, regionaal of nationaal.",

    "permit_planned_lead_time_days":
        "Geplande doorlooptijd van de vergunning met de langste verwachte afhandelingsduur, uitgedrukt in dagen.",

    # Cause 29
    "historical_weather_affected_days":
        "Gemiddeld aantal dagen per jaar waarop de locatie historisch wordt beïnvloed door ongunstige weersomstandigheden.",

    "weather_contingency_included":
        "Geeft aan of maatregelen voor weergerelateerde vertragingen zijn opgenomen.",

    "weather_sensitive_activities_share_pct":
        "Percentage van de geplande activiteiten dat gevoelig is voor ongunstige weersomstandigheden.",

    # Cause 30
    "geotechnical_investigation_completed":
        "Geeft aan of vóór start uitvoering een geotechnisch onderzoek is uitgevoerd.",

    # Cause 31
    "contractor_safety_record_trir":
        "Indicator voor de veiligheidsprestatie van de aannemer, zoals de Total Recordable Incident Rate (TRIR).",

    "safety_management_plan_in_place":
        "Geeft aan of vóór start uitvoering een formeel veiligheidsmanagementplan is vastgesteld.",

    "safety_certification_requirement":
        "Geeft aan of vereiste veiligheids­certificeringen, zoals SCC of VCA, aanwezig zijn.",

    "high_risk_activities_identified_count":
        "Aantal hoog-risicoactiviteiten dat vóór start uitvoering is geïdentificeerd.",

    "safety_training_hours_required":
        "Aantal veiligheidsopleidingsuren dat per werknemer is vereist.",

    # Cause 32
    "inflation_forecast_pct":
        "Verwachte inflatie bij projectstart, uitgedrukt als percentage.",

    "price_escalation_clauses_included":
        "Geeft aan of contractuele prijsescalatieclausules zijn opgenomen.",

    "pricing_mechanism":
        "Toegepast prijsmechanisme, geclassificeerd als vast of variabel (bijvoorbeeld cost-plus).",

    "contract_value_subject_to_indexation_pct":
        "Percentage van de totale contractwaarde dat onderhevig is aan prijsindexering.",

    # Cause 33
    "approvals_pending_count":
        "Aantal regelgevende of administratieve goedkeuringen dat bij start uitvoering nog openstaat.",

    "compliance_deliverables_required_count":
        "Aantal compliance-gerelateerde documenten of opleveringen dat tijdens de uitvoering vereist is.",

    # Cause 34
    "urban_context":
        "Classificatie van de projectlocatie als landelijk, suburbaan of sterk stedelijk.",

    "external_stakeholders_count":
        "Aantal externe stakeholders dat bij het project betrokken is.",

    "outstanding_stakeholder_objections_count":
        "Aantal onopgeloste bezwaren van stakeholders bij start uitvoering.",

    "traffic_management_plan":
        "Geeft aan of een verkeersmanagementplan is opgesteld of vereist.",

    "stakeholder_engagement_plan_in_place":
        "Geeft aan of een formeel stakeholdermanagementplan is vastgesteld.",

    # Cause 35
    "cost_contingency_included_pct":
        "Percentage kostencontingentie dat in de projectkostenraming is opgenomen.",

    "benchmarking_against_similar_projects_performed":
        "Geeft aan of bij de kostenraming gebruik is gemaakt van benchmarking of referentieprojecten.",

    # Context
    "planned_project_duration_days":
        "Geplande doorlooptijd van het project uitgedrukt in kalenderdagen."
}

var_units_dutch = {

    # Cause 1
    "schedule_level_of_detail_avg_activity_days": "Gemiddelde activiteitsduur (dagen)",

    # Cause 2
    "project_controls_plan_in_place": "Ja / Nee",
    "roles_responsibilities_defined_raci": "Ja / Nee",
    "site_logistics_plan_completed": "Ja / Nee",
    "quality_management_plan_in_place_qmp": "Ja / Nee",

    # Cause 3
    "scope_definition_completeness_pct": "Percentage WBS-elementen gespecificeerd (%)",
    "provisional_sums_pct_contract_value": "Percentage contractwaarde (%)",
    "change_control_procedure_defined": "Ja / Nee",

    # Cause 4
    "approval_layers_count": "Aantal",
    "approval_responsibility_allocation": "Opdrachtgever / Adviseur / Gezamenlijk",

    # Cause 5
    "clash_detection_performed_if_bim": "Ja / Nee",

    # Cause 6
    "design_schedule_baseline_approved": "Ja / Nee",
    "percentage_design_complete_at_award_pct": "%",
    "outstanding_design_packages_at_execution_start_count": "Aantal",

    # Cause 7
    "lead_designer_experience_years": "Jaren",
    "similar_projects_designed_count": "Aantal",
    "design_team_size_fte": "FTE",
    "bim_capability": "Ja / Nee",

    # Cause 8
    "financial_prequalification_score_0_100": "Score (0–100)",
    "contract_value_vs_annual_turnover_pct": "%",
    "proof_of_financing_submitted": "Ja / Nee",

    # Cause 9
    "contractual_payment_terms_days": "Dagen",
    "payment_security_instrument_included": "Ja / Nee",
    "owner_financial_reliability": "Laag / Middel / Hoog",

    # Cause 10
    "contractual_decision_time_days": "Dagen",
    "escalation_path_defined": "Ja / Nee",

    # Cause 11
    "owner_involvement": "Laag / Middel / Hoog",
    "change_initiation_rights": "Opdrachtgever / Gezamenlijk / Aannemer",

    # Cause 12
    "land_acquisition_right_of_way_resolved": "Ja / Nee",
    "unresolved_utilities_present": "Ja / Nee",
    "unresolved_site_access_constraints": "Ja / Nee",

    # Cause 13
    "contractor_experience_years": "Jaren",
    "similar_projects_completed_count": "Aantal",
    "technical_tender_score_0_100": "Score (0–100)",

    # Cause 14
    "method_statement_completeness": "%",
    "share_first_time_methods_pct": "%",

    # Cause 15
    "subcontracting_share_pct": "%",
    "number_of_subcontractors_count": "Aantal",
    "critical_package_subcontractor_awarded_pre_start_pct": "%",

    # Cause 16
    "inspection_test_plan_defined_itp": "Ja / Nee",
    "complexity_of_construction_scope_major_packages_wbs_count": "Aantal (hoofdpakketten)",

    # Cause 17
    "meeting_frequency_meetings_per_month_count": "Aantal vergaderingen per maand",
    "information_management": "Ja / Nee",
    "number_of_key_stakeholders_count": "Aantal",

    # Cause 18
    "imported_material_dependency_pct": "%",
    "critical_materials_identified_count": "Aantal",
    "critical_materials_lead_time_gt_8_weeks_count": "Aantal",
    "single_source_critical_materials_count": "Aantal",

    # Cause 19 
    "planned_procurement_lead_time_days": "Dagen",
    "critical_materials_ordered_pre_start_pct": "%",
    "supplier_reliability_pct_on_time_deliveries": "Percentage tijdige leveringen (%)",

    # Cause 20
    "supplier_iso_9001_certified": "Ja / Nee",

    # Cause 21
    "equipment_availability_confirmed_pct_critical_equipment": "Percentage kritisch materieel (%)",
    "equipment_ownership": "Eigendom / Gehuurd / Gemengd",
    "avg_equipment_age_years": "Jaren",

    # Cause 22
    "avg_operator_experience_years": "Jaren",

    # Cause 23
    "labour_availability_pct_planned_available_vs_required": "Percentage beschikbaar / vereist (%)",
    "dependency_on_scarce_trades_pct": "Percentage arbeidsuren (%)",
    "use_of_agency_temporary_labour_pct": "Percentage arbeidsuren (%)",
    "critical_trades_confirmed_pct": "Percentage kritische vakgebieden (%)",

    # Cause 24
    "overtime_shift_work_planned": "Ja / Nee",
    "site_logistics_complexity": "Laag / Middel / Hoog",

    # Cause 25
    "share_of_certified_workers_pct": "%",
    "planned_onboarding_training_days": "Dagen",
    "avg_experience_of_workforce_years": "Jaren",

    # Cause 26
    "contract_type": "UAV 2012 / UAV‑GC 2025 / Overig",
    "collaborative_contracting_bouwteam": "Ja / Nee",
    "incentive_mechanisms_included": "Ja / Nee",
    "deviations_from_standard_terms": "Aantal",

    # Cause 27
    "ongoing_legal_disputes": "Ja / Nee",
    "project_parties_prior_collaboration": "Ja / Nee",

    # Cause 28
    "permits_required_count": "Aantal",
    "permits_obtained_at_start_pct": "%",
    "authority_involvement_level": "Lokaal / Regionaal / Nationaal",
    "permit_planned_lead_time_days": "Dagen",

    # Cause 29
    "historical_weather_affected_days": "Dagen per jaar",
    "weather_contingency_included": "Ja / Nee",
    "weather_sensitive_activities_share_pct": "%",

    # Cause 30
    "geotechnical_investigation_completed": "Ja / Nee",

    # Cause 31
    "contractor_safety_record_trir": "TRIR",
    "safety_management_plan_in_place": "Ja / Nee",
    "safety_certification_requirement": "Ja / Nee",
    "high_risk_activities_identified_count": "Aantal",
    "safety_training_hours_required": "Uren per persoon",

    # Cause 32
    "inflation_forecast_pct": "%",
    "price_escalation_clauses_included": "Ja / Nee",
    "pricing_mechanism": "Vast / Variabel (cost‑plus)",
    "contract_value_subject_to_indexation_pct": "%",

    # Cause 33
    "approvals_pending_count": "Aantal",
    "compliance_deliverables_required_count": "Aantal",

    # Cause 34
    "urban_context": "Landelijk / Suburbaan / Sterk stedelijk",
    "external_stakeholders_count": "Aantal",
    "outstanding_stakeholder_objections_count": "Aantal",
    "traffic_management_plan": "Ja / Nee",
    "stakeholder_engagement_plan_in_place": "Ja / Nee",

    # Cause 35
    "cost_contingency_included_pct": "%",
    "benchmarking_against_similar_projects_performed": "Ja / Nee"
}

group_labels_dutch = {
    "planning_control": "Planning en beheersing",
    "design_readiness_quality": "Ontwerpgereedheid en -kwaliteit",
    "scope_change_management": "Scope- en wijzigingsbeheer",
    "owner_governance": "Opdrachtgever en governance",
    "contract_commercial_structure": "Contractuele en commerciële structuur",
    "contractor_supply_chain_capability": "Aannemer- en supply chain-capaciteit",
    "labour_productivity": "Arbeid en productiviteit",
    "site_external_conditions": "Locatie- en externe omstandigheden",
    "safety_rework": "Veiligheid en herstelwerk",
    "context": "Context"
}

continuous_actionable = {
    # Planning & scheduling
    "schedule_level_of_detail_avg_activity_days",

    # Scope & design
    "scope_definition_completeness_pct",
    "provisional_sums_pct_contract_value",
    "percentage_design_complete_at_award_pct",
    "outstanding_design_packages_at_execution_start_count",

    # Governance & decision-making
    "approval_layers_count",
    "contractual_decision_time_days",

    # Design & expertise (beïnvloedbaar via inzet / vervanging / ondersteuning)
    "lead_designer_experience_years",
    "similar_projects_designed_count",
    "design_team_size_fte",

    # Financial & commercial (keuzes / structuren)
    "financial_prequalification_score_0_100",
    "contract_value_vs_annual_turnover_pct",
    "contract_value_subject_to_indexation_pct",
    "cost_contingency_included_pct",
    "deviations_from_standard_terms",

    # Payments
    "contractual_payment_terms_days",

    # Contractor capability
    "contractor_experience_years",
    "similar_projects_completed_count",
    "technical_tender_score_0_100",

    # Methods & execution
    "method_statement_completeness",
    "share_first_time_methods_pct",
    "complexity_of_construction_scope_major_packages_wbs_count",

    # Subcontracting & supply chain
    "subcontracting_share_pct",
    "number_of_subcontractors_count",
    "critical_package_subcontractor_awarded_pre_start_pct",
    "imported_material_dependency_pct",
    "critical_materials_identified_count",
    "critical_materials_lead_time_gt_8_weeks_count",
    "single_source_critical_materials_count",
    "planned_procurement_lead_time_days",
    "critical_materials_ordered_pre_start_pct",
    "supplier_reliability_pct_on_time_deliveries",

    # Equipment
    "equipment_availability_confirmed_pct_critical_equipment",
    "avg_equipment_age_years",

    # Labour
    "avg_operator_experience_years",
    "labour_availability_pct_planned_available_vs_required",
    "dependency_on_scarce_trades_pct",
    "use_of_agency_temporary_labour_pct",
    "critical_trades_confirmed_pct",
    "share_of_certified_workers_pct",
    "planned_onboarding_training_days",
    "avg_experience_of_workforce_years",

    # Stakeholders & permits
    "permits_required_count",
    "permits_obtained_at_start_pct",
    "permit_planned_lead_time_days",
    "external_stakeholders_count",
    "outstanding_stakeholder_objections_count",
    "approvals_pending_count",
    "compliance_deliverables_required_count",

    # Safety
    "contractor_safety_record_trir",
    "high_risk_activities_identified_count",
    "safety_training_hours_required",

    # Weather exposure (beïnvloedbaar via planning/fasering, niet historisch)
    "weather_sensitive_activities_share_pct",
}

binary_actionable = {
    "project_controls_plan_in_place",
    "roles_responsibilities_defined_raci",
    "site_logistics_plan_completed",
    "quality_management_plan_in_place_qmp",
    "change_control_procedure_defined",
    "clash_detection_performed_if_bim",
    "design_schedule_baseline_approved",
    "bim_capability",
    "proof_of_financing_submitted",
    "payment_security_instrument_included",
    "escalation_path_defined",
    "land_acquisition_right_of_way_resolved",
    "inspection_test_plan_defined_itp",
    "information_management",
    "supplier_iso_9001_certified",
    "overtime_shift_work_planned",
    "collaborative_contracting_bouwteam",
    "incentive_mechanisms_included",
    "project_parties_prior_collaboration",
    "weather_contingency_included",
    "geotechnical_investigation_completed",
    "safety_management_plan_in_place",
    "safety_certification_requirement",
    "price_escalation_clauses_included",
    "traffic_management_plan",
    "stakeholder_engagement_plan_in_place",
    "benchmarking_against_similar_projects_performed",
}

EXPERIMENT_SCENARIO_PRESET = {

    "planned_project_duration_days": 420,
    "schedule_level_of_detail_avg_activity_days": 10,

    "project_controls_plan_in_place": 1,
    "roles_responsibilities_defined_raci": 1,
    "site_logistics_plan_completed": 1,
    "quality_management_plan_in_place_qmp": 1,
    "information_management": 0,
    "design_schedule_baseline_approved": 1,

    "scope_definition_completeness_pct": 75,
    "provisional_sums_pct_contract_value": 15,
    "change_control_procedure_defined": 1,

    "percentage_design_complete_at_award_pct": 20,
    "outstanding_design_packages_at_execution_start_count": 7,
    "clash_detection_performed_if_bim": 1,
    "bim_capability": 1,

    "lead_designer_experience_years": 10,
    "similar_projects_designed_count": 8,
    "design_team_size_fte": 8,

    "approval_layers_count": 6,
    "contractual_decision_time_days": 42,
    "approval_responsibility_allocation": "Gezamenlijk",
    "owner_involvement": "Gemiddeld",
    "change_initiation_rights": "Gezamenlijk",
    "escalation_path_defined": 1,

    "owner_financial_reliability": "Hoog",
    "financial_prequalification_score_0_100": 90,
    "contract_value_vs_annual_turnover_pct": 40,
    "proof_of_financing_submitted": 1,
    "payment_security_instrument_included": 1,
    "contractual_payment_terms_days": 30,
    "contract_type": "UAV-GC 2025",
    "pricing_mechanism": "Vast",
    "price_escalation_clauses_included": 1,
    "inflation_forecast_pct": 4,
    "contract_value_subject_to_indexation_pct": 35,
    "deviations_from_standard_terms": 2,
    "collaborative_contracting_bouwteam": 0,
    "incentive_mechanisms_included": 1,
    "benchmarking_against_similar_projects_performed": 1,

    "contractor_experience_years": 15,
    "similar_projects_completed_count": 10,
    "technical_tender_score_0_100": 75,
    "method_statement_completeness": 70,
    "share_first_time_methods_pct": 25,
    "subcontracting_share_pct": 50,
    "number_of_subcontractors_count": 8,
    "critical_package_subcontractor_awarded_pre_start_pct": 50,
    "supplier_iso_9001_certified": 1,

    "imported_material_dependency_pct": 35,
    "critical_materials_identified_count": 6,
    "critical_materials_lead_time_gt_8_weeks_count": 4,
    "single_source_critical_materials_count": 2,
    "planned_procurement_lead_time_days": 65,
    "critical_materials_ordered_pre_start_pct": 30,
    "supplier_reliability_pct_on_time_deliveries": 90,

    "equipment_availability_confirmed_pct_critical_equipment": 85,
    "equipment_ownership": "Combinatie",
    "avg_equipment_age_years": 7,
    "avg_operator_experience_years": 8,

    "labour_availability_pct_planned_available_vs_required": 82,
    "dependency_on_scarce_trades_pct": 45,
    "use_of_agency_temporary_labour_pct": 20,
    "critical_trades_confirmed_pct": 70,
    "overtime_shift_work_planned": 0,
    "share_of_certified_workers_pct": 65,
    "planned_onboarding_training_days": 5,
    "avg_experience_of_workforce_years": 9,

    "permits_required_count": 13,
    "permits_obtained_at_start_pct": 20,
    "permit_planned_lead_time_days": 170,
    "approvals_pending_count": 7,
    "authority_involvement_level": "Nationaal",
    "compliance_deliverables_required_count": 12,

    "urban_context": "Dicht stedelijk",
    "external_stakeholders_count": 10,
    "outstanding_stakeholder_objections_count": 2,
    "traffic_management_plan": 1,
    "stakeholder_engagement_plan_in_place": 1,
    "unresolved_utilities_present": 1,
    "unresolved_site_access_constraints": 1,
    "land_acquisition_right_of_way_resolved": 1,
    "geotechnical_investigation_completed": 1,

    "historical_weather_affected_days": 20,
    "weather_sensitive_activities_share_pct": 60,
    "weather_contingency_included": 1,

    "inspection_test_plan_defined_itp": 1,
    "complexity_of_construction_scope_major_packages_wbs_count": 9,
    "contractor_safety_record_trir": 1.4,
    "safety_management_plan_in_place": 1,
    "safety_certification_requirement": 1,
    "high_risk_activities_identified_count": 4,
    "safety_training_hours_required": 8,

    "ongoing_legal_disputes": 1,
    "project_parties_prior_collaboration": 0,

    "cost_contingency_included_pct": 10,

    "cost_estimate_class_aace_1_5": "Klasse 3",
    "meeting_frequency_meetings_per_month_count": 4,
    "site_logistics_complexity": "Hoog"

}
