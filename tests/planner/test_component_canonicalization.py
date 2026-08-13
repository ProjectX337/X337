from core.planner.project_planner import ProjectPlanner


def test_feature_components_materialize_in_canonical_ui_spec():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication, AI assistant, analytics, dashboard, users, and search"
    )

    canonical = {
        component.name: component
        for component in spec.ui_spec.component_models
    }

    feature_components = {
        component
        for feature in spec.feature_models
        for component in feature.components
    }

    assert "SearchBar" in canonical

    for component_name in feature_components:
        assert component_name in canonical


def test_feature_component_ownership_is_preserved():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication, AI assistant, analytics, dashboard, users, and search"
    )

    canonical = {
        component.name: component
        for component in spec.ui_spec.component_models
    }

    expected = {
        "ChatPanel": {"ai"},
        "MetricCard": {"analytics"},
        "Navbar": {"dashboard"},
        "Sidebar": {"dashboard"},
        "DashboardCard": {"dashboard"},
        "PromptBox": {"ai"},
        "Chart": {"analytics"},
        "ReportTable": {"analytics"},
        "AuthForm": {"authentication"},
        "UserMenu": {"authentication"},
        "UserTable": {"users"},
        "SearchBar": {"search"},
    }

    for name, features in expected.items():
        assert name in canonical

        actual = set(
            canonical[name].metadata.get("features", [])
        )

        assert features.issubset(actual), (
            f"{name}: expected {features}, got {actual}"
        )
