from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ParsedIntent:

    project_type: str = ""

    description: str = ""

    features: list[str] = None


class PromptParser:
    """
    Converts user language into project intent.
    """

    def parse(
        self,
        message: str,
    ) -> ParsedIntent:

        text = message.lower()

        features = []

        if "auth" in text:
            features.append(
                "authentication"
            )

        if "dashboard" in text:
            features.append(
                "dashboard"
            )

        if "billing" in text:
            features.append(
                "billing"
            )

        return ParsedIntent(
            project_type="application",
            description=message,
            features=features,
        )
