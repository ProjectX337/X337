from __future__ import annotations


class ChangeEngine:
    """
    Converts user requests into project modifications.
    """


    def detect(
        self,
        message: str,
    ) -> dict:

        text = message.lower()

        changes = []


        if "auth" in text:

            changes.append(
                "authentication"
            )


        if "billing" in text:

            changes.append(
                "billing"
            )


        if "dashboard" in text:

            changes.append(
                "dashboard"
            )


        return {
            "features": changes
        }
