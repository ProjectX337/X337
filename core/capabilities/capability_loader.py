from __future__ import annotations

import json
from pathlib import Path

from core.capabilities.capability import Capability


class CapabilityLoader:
    """
    Loads capability definitions from JSON files.
    """

    def __init__(
        self,
        directory: str = "capabilities",
    ):

        self.directory = Path(directory)

    # ---------------------------------------------------------

    def load(
        self,
    ) -> list[Capability]:

        capabilities: list[Capability] = []

        if not self.directory.exists():
            return capabilities

        for file in sorted(
            self.directory.glob("*.json")
        ):

            with file.open(
                "r",
                encoding="utf-8",
            ) as f:

                data = json.load(f)

            capabilities.append(

                Capability(

                    name=data["name"],

                    description=data.get(
                        "description",
                        "",
                    ),

                    keywords=data.get(
                        "keywords",
                        [],
                    ),

                    technologies=data.get(
                        "technologies",
                        [],
                    ),

                    required_roles=data.get(
                        "required_roles",
                        [],
                    ),

                    pages=data.get(
                        "pages",
                        [],
                    ),

                    components=data.get(
                        "components",
                        [],
                    ),

                    priority=data.get(
                        "priority",
                        100,
                    ),

                    metadata=data.get(
                        "metadata",
                        {},
                    ),

                )

            )

        return capabilities
