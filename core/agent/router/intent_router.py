from __future__ import annotations


class IntentRouter:
    """
    Determines what X337 should do next.
    """

    def classify(
        self,
        message: str,
    ) -> str:

        text = message.lower()


        if any(
            word in text
            for word in [
                "fix",
                "error",
                "broken",
                "bug",
                "repair",
            ]
        ):
            return "repair"


        if any(
            word in text
            for word in [
                "add",
                "change",
                "update",
                "modify",
                "improve",
            ]
        ):
            return "modify"


        return "build"
