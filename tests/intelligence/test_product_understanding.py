from core.intelligence.models import ProductIntent
from core.intelligence.synthesis import (
    ProductUnderstandingSynthesizer,
)


def test_product_understanding_synthesis():

    intent = ProductIntent(
        domain="education",
        goals=[
            "help students learn"
        ],
        capabilities=[
            "adaptive lessons"
        ],
    )

    result = (
        ProductUnderstandingSynthesizer()
        .synthesize(intent)
    )

    assert result.domain == "education"
    assert "adaptive lessons" in result.capabilities
