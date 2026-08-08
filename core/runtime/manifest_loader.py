import json
from pathlib import Path

from core.runtime.artifact import Artifact


class ManifestLoader:

    def __init__(self, manifest_dir="workspace/manifests"):
        self.manifest_dir = Path(manifest_dir)


    def load(self, name):

        path = self.manifest_dir / f"{name}.json"

        with open(path, "r") as file:
            data = json.load(file)

        return Artifact(
            name=data["name"],
            artifact_type=data["type"],
            path=data["path"],
            framework=data.get("framework"),
            install_commands=data.get(
                "install_commands",
                []
            ),
            run_commands=data.get(
                "run_commands",
                []
            ),
            preview_port=data.get(
                "preview_port"
            )
        )


    def list_manifests(self):

        return [
            file.stem
            for file in self.manifest_dir.glob("*.json")
        ]
