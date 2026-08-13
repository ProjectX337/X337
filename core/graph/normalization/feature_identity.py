from __future__ import annotations


FEATURE_ALIASES = {
    "ai_assistant": "ai",
    "chat": "ai",
}


def normalize_feature_slug(value: str) -> str:
    normalized = (
        str(value)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )

    return FEATURE_ALIASES.get(
        normalized,
        normalized,
    )
