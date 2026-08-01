from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Conversation:
    """
    Stores an X337 builder conversation.
    """

    messages: list[dict[str, str]] = field(
        default_factory=list
    )

    project_name: str = ""

    last_prompt: str = ""

    def add(
        self,
        role: str,
        content: str,
    ) -> None:

        self.messages.append(
            {
                "role": role,
                "content": content,
            }
        )
