from __future__ import annotations


PAGE_ALIASES = {
    "login_page": "login",
    "signin": "login",
    "sign_in": "login",
    "signup": "signup",
    "register": "signup",
    "registration": "signup",
}


def normalize_page_slug(
    value: str,
) -> str:

    normalized = (
        str(value)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )

    return PAGE_ALIASES.get(
        normalized,
        normalized,
    )
