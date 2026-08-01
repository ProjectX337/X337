from dataclasses import dataclass, field

from core.agent.messages import Message


@dataclass
class Conversation:

    messages: list[Message] = field(
        default_factory=list
    )

    def add(
        self,
        role: str,
        content: str,
    ):
        self.messages.append(
            Message(
                role=role,
                content=content,
            )
        )
