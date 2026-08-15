from __future__ import annotations

from core.capabilities.capability_registry import (
    CapabilityRegistry,
)


# ------------------------------------------------------------------
# Semantic capability phrases
#
# These are product-language expressions, not parser keywords.
# Outputs MUST be canonical CapabilityRegistry names.
# ------------------------------------------------------------------

CAPABILITY_PHRASES: dict[str, str] = {
    # AI
    "ai assistant": "ai",
    "ai assistants": "ai",
    "ai assistant": "ai",
    "assistant": "ai",
    "copilot": "ai",
    "llm": "ai",

    # Authentication
    "authentication": "authentication",
    "authenticate": "authentication",
    "login": "authentication",
    "log in": "authentication",
    "sign in": "authentication",
    "signin": "authentication",
    "signup": "authentication",
    "sign up": "authentication",

    # Analytics
    "analytics": "analytics",
    "insights": "analytics",
    "metrics": "analytics",
    "reporting": "reporting",
    "reports": "reporting",

    # Dashboard
    "dashboard": "dashboard",
    "overview": "dashboard",

    # Users
    "user management": "users",
    "manage users": "users",
    "managing users": "users",
    "manage user": "users",
    "managing user": "users",
    "users": "users",
    "user": "users",
    "accounts": "users",
    "account": "users",

    # Search
    "search": "search",
    "searching": "search",
    "find": "search",
    "lookup": "search",

    # Chat
    "chat": "chat",
    "messaging": "chat",
    "messages": "chat",
    "conversation": "chat",
    "conversations": "chat",

    # Billing / payments
    "billing": "billing",
    "payments": "payments",
    "payment": "payments",
    "checkout": "payments",
    "subscription": "billing",
    "subscriptions": "billing",

    # Settings
    "settings": "settings",
    "preferences": "settings",
    "configuration": "settings",

    # Calendar
    "calendar": "calendar",
    "scheduling": "calendar",
    "schedule": "calendar",
    "events": "calendar",

    # Tasks
    "tasks": "tasks",
    "task management": "tasks",
    "todo": "tasks",

    # Notifications
    "notifications": "notifications",
    "alerts": "notifications",

    # Teams
    "team management": "team_management",
    "teams": "team_management",
    "team": "team_management",
    "members": "team_management",
    "organization": "team_management",

    # File upload
    "file upload": "file_upload",
    "file uploads": "file_upload",
    "upload": "file_upload",
    "attachments": "file_upload",
    "attachment": "file_upload",

    # CRM
    "crm": "crm",
    "customer management": "crm",
    "customers": "crm",
    "contacts": "crm",
    "leads": "crm",

    # Administration
    "admin": "admin",
    "administration": "admin",
    "administrator": "admin",
}


def infer_capabilities(
    text: str,
) -> list[str]:
    """
    Infer canonical product capabilities from natural-language
    product requirements.

    This function produces semantic capability names only.

    It deliberately does NOT consume ParsedPrompt.keywords,
    because parser keywords are lexical evidence rather than
    product capabilities.

    Canonical capability names are validated against the
    CapabilityRegistry.
    """

    normalized = " ".join(
        text.lower().split()
    )

    registry = CapabilityRegistry()

    capabilities: list[str] = []

    for phrase, capability_name in sorted(
        CAPABILITY_PHRASES.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    ):
        if phrase not in normalized:
            continue

        if registry.get(capability_name) is None:
            continue

        if capability_name not in capabilities:
            capabilities.append(
                capability_name
            )

    return capabilities
