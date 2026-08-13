from core.dashboard.generator_server import apply_training_profile
from core.planner.project_planner import ProjectPlanner


def test_training_profile_changes_canonical_design_tokens():
    spec = ProjectPlanner().plan(
        "Build a dark futuristic SaaS dashboard"
    )

    apply_training_profile(
        spec,
        [
            {
                "name": "Reference",
                "profile": {
                    "visual_style": "dark futuristic glassmorphism",
                    "colors": [
                        "#050816",
                        "#111827",
                        "#7C3AED",
                        "#06B6D4",
                        "#22D3EE",
                        "#F8FAFC",
                        "#94A3B8",
                    ],
                    "fonts": [
                        "Space Grotesk",
                        "JetBrains Mono",
                    ],
                    "spacing_values": [
                        "4px",
                        "64px",
                        "1200px",
                    ],
                    "layout_patterns": [
                        "glass",
                        "gradient",
                        "responsive",
                    ],
                    "component_patterns": [
                        "Card",
                        "Sidebar",
                    ],
                    "interaction_patterns": [
                        "buttons",
                        "navigation",
                    ],
                    "keywords": [
                        "dark",
                        "futuristic",
                    ],
                },
            }
        ],
    )

    design = spec.ui_spec.design_system

    assert design.colors["background"] == "#050816"
    assert design.colors["primary"] == "#7C3AED"
    assert design.typography["heading"] == "Space Grotesk"
    assert design.typography["body"] == "Space Grotesk"
    assert design.spacing["section"] == "64px"

    assert "training_profile" in design.metadata


def test_training_profile_without_tokens_preserves_defaults():
    spec = ProjectPlanner().plan(
        "Build a modern application"
    )

    original_colors = dict(
        spec.ui_spec.design_system.colors
    )

    apply_training_profile(
        spec,
        [
            {
                "name": "Reference",
                "profile": {
                    "visual_style": "modern",
                    "colors": [],
                    "fonts": [],
                    "spacing_values": [],
                    "layout_patterns": [],
                    "component_patterns": [],
                    "interaction_patterns": [],
                    "keywords": [],
                },
            }
        ],
    )

    assert (
        spec.ui_spec.design_system.colors
        == original_colors
    )


def test_training_spacing_roles_apply_semantically():
    from core.dashboard.generator_server import apply_training_profile
    from core.planner.project_planner import ProjectPlanner

    spec = ProjectPlanner().plan(
        "Build a dark futuristic SaaS dashboard"
    )

    apply_training_profile(
        spec,
        [
            {
                "name": "Spacing Reference",
                "profile": {
                    "spacing_values": [
                        "24px",
                        "32px",
                        "12px",
                        "18px",
                    ],
                    "spacing_roles": {
                        "compact": ["12px"],
                        "comfortable": [
                            "24px",
                            "32px",
                            "18px",
                        ],
                        "spacious": [],
                    },
                },
            }
        ],
    )

    spacing = spec.ui_spec.design_system.spacing

    assert spacing["unit"] == "12px"
    assert spacing["section"] == "32px"
    assert spacing["container"] != "12px"
