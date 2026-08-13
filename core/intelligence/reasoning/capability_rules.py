from __future__ import annotations


CAPABILITY_RULES = {

    "learning assistant": [
        "ai",
        "chat",
        "search",
        "analytics",
    ],

    "crm": [
        "users",
        "dashboard",
        "analytics",
    ],

    "ecommerce": [
        "payments",
        "search",
        "users",
    ],

}


def infer_capabilities(text: str) -> list[str]:

    text = text.lower()

    capabilities = set()

    for pattern, items in CAPABILITY_RULES.items():

        if pattern in text:

            capabilities.update(
                items
            )

    return sorted(
        capabilities
    )
