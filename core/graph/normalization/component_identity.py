from __future__ import annotations


COMPONENT_ALIASES = {
    "chat_panel": "chatpanel",
    "chat-panel": "chatpanel",
    "prompt_box": "promptbox",
    "prompt-box": "promptbox",
    "message_bubble": "messagebubble",
    "message-bubble": "messagebubble",
}


def normalize_component_slug(
    value: str,
) -> str:

    normalized = (
        str(value)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )

    return COMPONENT_ALIASES.get(
        normalized,
        normalized.replace("_", ""),
    )
