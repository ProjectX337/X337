from __future__ import annotations

from core.memory.memory_manager import MemoryManager


class ConversationMemory:

    def __init__(self):
        self.memory = MemoryManager()


    def add_turn(
        self,
        message,
        intent,
    ):

        history = self.memory.recall(
            "conversation_history",
            []
        )

        history.append(
            {
                "message": message,
                "intent": intent,
            }
        )

        self.memory.remember(
            "conversation_history",
            history,
        )

        return history


    def history(self):

        return self.memory.recall(
            "conversation_history",
            []
        )
