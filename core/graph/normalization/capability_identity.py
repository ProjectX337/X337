from __future__ import annotations


CAPABILITY_ALIASES = {
    "chat": "ai",
}


def normalize_capability_slug(
    value: str,
) -> str:

    normalized = (
        str(value)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )

    return CAPABILITY_ALIASES.get(
        normalized,
        normalized,
    )
