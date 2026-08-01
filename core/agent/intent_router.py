from __future__ import annotations


class IntentRouter:
    """
    Determines what the user wants X337 to do.
    """

    def route(
        self,
        message: str,
    ) -> str:

        text = message.lower()

        if "build" in text:
            return "create_project"

        if "add" in text:
            return "modify_project"

        if "fix" in text:
            return "repair_project"

        return "general_question"
