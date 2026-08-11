from __future__ import annotations

import json
from pathlib import Path

from core.capabilities.capability import Capability


class CapabilityLoader:
    """
    Loads canonical capability definitions from JSON files.

    JSON is normalized at the loader boundary so every downstream
    planner receives the same canonical Capability representation.
    """

    def __init__(
        self,
        directory: str = "capabilities",
    ) -> None:
        self.directory = Path(directory)

    def load(self) -> list[Capability]:
        capabilities: list[Capability] = []

        if not self.directory.exists():
            return capabilities

        for file in sorted(
            self.directory.glob("*.json")
        ):
            with file.open(
                "r",
                encoding="utf-8",
            ) as handle:
                data = json.load(handle)

            metadata = dict(
                data.get(
                    "metadata",
                    {},
                )
            )

            # -------------------------------------------------
            # Normalize feature definitions.
            #
            # Canonical storage is metadata.features, but older
            # capability files may still define features at the
            # top level.
            # -------------------------------------------------

            if (
                "features" in data
                and "features" not in metadata
            ):
                metadata["features"] = data["features"]

            features = list(
                metadata.get(
                    "features",
                    [],
                )
            )

            # -------------------------------------------------
            # Normalize API definitions.
            # -------------------------------------------------

            if (
                "api_endpoints" in data
                and "api_endpoints" not in metadata
            ):
                metadata["api_endpoints"] = data[
                    "api_endpoints"
                ]

            # -------------------------------------------------
            # Derive canonical pages/components/APIs from
            # feature definitions when the capability JSON
            # does not explicitly provide them.
            # -------------------------------------------------

            pages = list(
                data.get(
                    "pages",
                    [],
                )
            )

            components = list(
                data.get(
                    "components",
                    [],
                )
            )

            endpoints = list(
                metadata.get(
                    "api_endpoints",
                    [],
                )
            )

            for feature in features:
                for page in feature.get(
                    "pages",
                    [],
                ):
                    if page not in pages:
                        pages.append(page)

                for component in feature.get(
                    "components",
                    [],
                ):
                    if component not in components:
                        components.append(component)

                for endpoint in feature.get(
                    "api_endpoints",
                    [],
                ):
                    if endpoint not in endpoints:
                        endpoints.append(endpoint)

            # Keep canonical metadata synchronized.
            metadata["features"] = features
            metadata["api_endpoints"] = endpoints

            capabilities.append(
                Capability(
                    name=data["name"],
                    description=data.get(
                        "description",
                        "",
                    ),
                    keywords=list(
                        data.get(
                            "keywords",
                            [],
                        )
                    ),
                    technologies=list(
                        data.get(
                            "technologies",
                            [],
                        )
                    ),
                    required_roles=list(
                        data.get(
                            "required_roles",
                            [],
                        )
                    ),
                    pages=pages,
                    components=components,
                    priority=int(
                        data.get(
                            "priority",
                            100,
                        )
                    ),
                    confidence=float(
                        data.get(
                            "confidence",
                            1.0,
                        )
                    ),
                    depends_on=list(
                        data.get(
                            "depends_on",
                            [],
                        )
                    ),
                    implies=list(
                        data.get(
                            "implies",
                            [],
                        )
                    ),
                    conflicts_with=list(
                        data.get(
                            "conflicts_with",
                            [],
                        )
                    ),
                    metadata=metadata,
                )
            )

        return capabilities
