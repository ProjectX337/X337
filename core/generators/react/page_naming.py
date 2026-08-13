from __future__ import annotations

import re


def page_filename(name: str) -> str:
    """
    Return the canonical generated filename/route segment for a page.

    Examples:
        AI                  -> ai
        Dashboard           -> dashboard
        User Settings       -> user-settings
        AISettings          -> ai-settings
        AccountOverview     -> account-overview
        Recent Transactions -> recent-transactions
        API                 -> api
        API Settings        -> api-settings
    """

    value = str(name).strip()

    # Split acronym/camel-case boundaries:
    # "AISettings" -> "AI Settings"
    value = re.sub(
        r"([A-Z]+)([A-Z][a-z])",
        r"\1 \2",
        value,
    )

    # Split normal camel-case boundaries:
    # "AccountOverview" -> "Account Overview"
    value = re.sub(
        r"([a-z0-9])([A-Z])",
        r"\1 \2",
        value,
    )

    # Normalize punctuation/whitespace to a single separator.
    value = re.sub(
        r"[^a-zA-Z0-9]+",
        "-",
        value,
    )

    return value.strip("-").lower()
