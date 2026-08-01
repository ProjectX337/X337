from __future__ import annotations

import json
from pathlib import Path

from core.registry.architecture import Architecture


class PluginLoader:
    """
    Loads Architecture plugins from the plugins directory.
    """

    def __init__(
        self,
        plugin_directory: str = "plugins",
    ):

        self.directory = Path(plugin_directory)

    # ---------------------------------------------------------

    def load(self) -> list[Architecture]:

        architectures: list[Architecture] = []

        if not self.directory.exists():
            return architectures

        for plugin in sorted(self.directory.iterdir()):

            if not plugin.is_dir():
                continue

            manifest = plugin / "manifest.json"

            if not manifest.exists():
                continue

            with manifest.open(
                "r",
                encoding="utf-8",
            ) as f:

                data = json.load(f)

            architecture = Architecture(

                name=data["name"],

                language=data["language"],

                template=data["template"],

                tester=data["tester"],

                keywords=data.get(
                    "keywords",
                    [],
                ),

                dependencies=data.get(
                    "dependencies",
                    [],
                ),

                default_features=data.get(
                    "default_features",
                    [],
                ),

                roles=data.get(
                    "roles",
                    [],
                ),

                technology_defaults=data.get(
                    "technology_defaults",
                    {},
                ),

                metadata=data.get(
                    "metadata",
                    {},
                ),

            )

            architectures.append(
                architecture
            )

        return architectures