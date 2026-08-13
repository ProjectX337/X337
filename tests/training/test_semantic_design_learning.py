from core.training.training_intelligence import TrainingIntelligence


REFERENCE = """
.dashboard {
    display: grid;
    grid-template-columns: 260px 1fr;
    min-height: 100vh;
    background: #070B16;
    color: #F8FAFC;
}

.sidebar {
    padding: 24px;
    background: rgba(15, 23, 42, 0.82);
    border-radius: 20px;
    backdrop-filter: blur(20px);
}

.content {
    padding: 32px;
}

.card {
    padding: 24px;
    border-radius: 20px;
    background: linear-gradient(
        180deg,
        rgba(17,24,39,0.92),
        rgba(17,24,39,0.68)
    );
}

.primary {
    background: #7C3AED;
    color: #FFFFFF;
    border-radius: 12px;
}

h1 {
    font-family: Inter, sans-serif;
}
"""


def test_semantic_design_learning():
    profile = TrainingIntelligence().analyze(
        name="Semantic Dashboard",
        description=(
            "Dark futuristic SaaS dashboard "
            "with glassmorphism and gradients"
        ),
        code=REFERENCE,
    ).to_dict()

    assert "#070B16" in profile["colors"]
    assert "#7C3AED" in profile["colors"]

    assert "Inter, sans-serif" in profile["fonts"]

    assert "grid" in profile["layout_patterns"]
    assert "sidebar" in profile["layout_patterns"]
    assert "cards" in profile["layout_patterns"]
    assert "glass" in profile["layout_patterns"]
    assert "gradient" in profile["layout_patterns"]

    assert "20px" in profile["radius_values"]
    assert "260px" not in profile["radius_values"]
    assert "100vh" not in profile["radius_values"]


def test_semantic_color_roles():
    profile = TrainingIntelligence().analyze(
        name="Color Role Test",
        description="Dark SaaS dashboard",
        code="""
        :root {
            color: #F8FAFC;
            background: #070B16;
        }

        .dashboard {
            background: #070B16;
        }

        .sidebar {
            background: rgba(15, 23, 42, 0.82);
        }

        .card {
            background: linear-gradient(
                180deg,
                rgba(17,24,39,0.92),
                rgba(17,24,39,0.68)
            );
            color: #F8FAFC;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .muted {
            color: #94A3B8;
        }

        .primary {
            background: #7C3AED;
        }
        """,
    ).to_dict()

    roles = profile["color_roles"]

    assert "#070B16" in roles["background"]
    assert "#F8FAFC" in roles["text"]

    assert "#94A3B8" in roles["muted"]

    assert (
        "rgba(15, 23, 42, 0.82)"
        in roles["surface"]
    )

    assert (
        "rgba(255,255,255,0.08)"
        in roles["border"]
    )

    assert "#7C3AED" in (
        roles["background"]
        or []
    ) or "#7C3AED" in (
        roles.get("primary", [])
    )


def test_semantic_color_roles_do_not_cross_contaminate():
    profile = TrainingIntelligence().analyze(
        name="Strict Color Test",
        description="Dark futuristic SaaS dashboard",
        code="""
        :root {
            background: #070B16;
            color: #F8FAFC;
        }

        .sidebar {
            background: rgba(15, 23, 42, 0.82);
        }

        .card {
            background: rgba(17, 24, 39, 0.92);
            border: 1px solid rgba(255,255,255,0.08);
        }

        .muted {
            color: #94A3B8;
        }

        .primary {
            background: #7C3AED;
        }
        """,
    ).to_dict()

    roles = profile["color_roles"]

    assert roles["background"] == ["#070B16"]
    assert "#F8FAFC" not in roles["background"]

    assert "#F8FAFC" in roles["text"]
    assert "#94A3B8" in roles["muted"]

    assert (
        "rgba(15, 23, 42, 0.82)"
        in roles["surface"]
    )

    assert (
        "rgba(17, 24, 39, 0.92)"
        in roles["surface"]
    )

    assert "#7C3AED" in roles["primary"]
    assert "#7C3AED" in roles["accent"]

    assert (
        "rgba(255,255,255,0.08)"
        in roles["border"]
    )
