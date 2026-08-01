from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ConversationMemory:

    messages: list[str] = field(
        default_factory=list
    )

    def add(
        self,
        message: str,
    ):
        self.messages.append(message)


    def history(self):
        return self.messages
