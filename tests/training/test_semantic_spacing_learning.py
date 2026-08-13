from core.training.training_intelligence import TrainingIntelligence


REFERENCE = """
.dashboard {
    padding: 24px;
    margin: 0 auto;
    gap: 16px;
    row-gap: 12px;
    column-gap: 20px;
}

.card {
    padding: 20px;
    border-radius: 20px;
}

.section {
    margin: 32px;
}

.container {
    max-width: 1200px;
    min-height: 100vh;
}
"""


def test_semantic_spacing_learning():
    profile = TrainingIntelligence().analyze(
        name="Spacing Reference",
        description="Responsive SaaS dashboard",
        code=REFERENCE,
    ).to_dict()

    assert "20px" in profile["radius_values"]

    assert "24px" in profile["spacing_values"]
    assert "16px" in profile["spacing_values"]
    assert "12px" in profile["spacing_values"]
    assert "20px" in profile["spacing_values"]
    assert "32px" in profile["spacing_values"]

    assert "1200px" not in profile["spacing_values"]
    assert "100vh" not in profile["spacing_values"]


def test_spacing_roles_are_semantic():
    profile = TrainingIntelligence().analyze(
        name="Spacing Reference",
        description="Responsive SaaS dashboard",
        code=REFERENCE,
    ).to_dict()

    roles = profile["spacing_roles"]

    assert "12px" in roles["compact"]
    assert "16px" in roles["compact"]
    assert "20px" in roles["comfortable"]
    assert "24px" in roles["comfortable"]
    assert "32px" in roles["comfortable"]
