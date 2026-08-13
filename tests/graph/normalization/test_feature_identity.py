from core.graph.normalization.feature_normalizer import (
    FeatureNormalizer,
)
from core.spec.models.feature_spec import FeatureSpec


def test_feature_identity_normalization():

    features = [
        FeatureSpec(
            name="AI Assistant",
            slug="ai",
        ),
        FeatureSpec(
            name="Chat",
            slug="chat",
        ),
    ]

    normalized = FeatureNormalizer().normalize(
        features
    )

    slugs = {
        feature.slug
        for feature in normalized
    }

    assert "ai" in slugs
    assert "chat" not in slugs
