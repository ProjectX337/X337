from core.graph.normalization.capability_normalizer import (
    CapabilityNormalizer,
)

from core.graph.normalization.capability_identity import (
    normalize_capability_slug,
)

from core.graph.normalization.feature_identity import (
    normalize_feature_slug,
)

__all__ = [
    "CapabilityNormalizer",
    "normalize_capability_slug",
    "normalize_feature_slug",
]
