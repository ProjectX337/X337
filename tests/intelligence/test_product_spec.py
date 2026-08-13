from core.intelligence.product_spec import ProductSpec


def test_product_spec_contract():

    spec = ProductSpec(
        name="AI Tutor",
        product_type="education",
        features=[
            "adaptive learning"
        ],
        entities=[
            "student"
        ],
    )

    data = spec.as_dict()

    assert data["name"] == "AI Tutor"
    assert "adaptive learning" in data["features"]
    assert "student" in data["entities"]
