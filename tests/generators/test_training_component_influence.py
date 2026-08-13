from core.planner.project_planner import ProjectPlanner
from core.dashboard.generator_server import apply_training_profile


def test_training_component_roles_reach_components():

    spec = ProjectPlanner().plan(
        "Build a SaaS dashboard"
    )

    apply_training_profile(
        spec,
        [
            {
                "name": "Dashboard Reference",
                "profile": {
                    "component_roles": {
                        "Navbar": {
                            "role": "navigation",
                            "patterns": [
                                "sticky",
                                "responsive",
                            ],
                        },
                        "Chart": {
                            "role": "visualization",
                            "patterns": [
                                "analytics",
                            ],
                        },
                    }
                },
            }
        ],
    )

    components = {
        c.name: c.metadata
        for c in spec.ui_spec.component_models
    }

    assert "Navbar" in components

    assert (
        components["Navbar"]["training_role"]
        == "navigation"
    )

    assert (
        "responsive"
        in components["Navbar"]["training_patterns"]
    )
