from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from core.training.training_intelligence import TrainingIntelligence
from datetime import datetime, timezone


@dataclass
class TrainingExample:
    name: str
    description: str
    code: str
    created_at: str


class TrainingStore:
    """
    Persistent local training corpus for X337.

    Training examples are stored as knowledge inputs rather
    than being injected blindly into generation prompts.
    """

    def __init__(
        self,
        path: str = "workspace/training/examples.json",
    ) -> None:
        self.path = Path(path)
        self.intelligence = TrainingIntelligence()

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _load(self) -> list[dict]:
        if not self.path.exists():
            return []

        try:
            return json.loads(
                self.path.read_text()
            )
        except (json.JSONDecodeError, OSError):
            return []

    def _save(self, items: list[dict]) -> None:
        self.path.write_text(
            json.dumps(
                items,
                indent=2,
            )
        )

    def add(
        self,
        *,
        name: str,
        description: str,
        code: str,
    ) -> TrainingExample:

        example = TrainingExample(
            name=name.strip() or "Untitled example",
            description=description.strip(),
            code=code,
            created_at=datetime.now(
                timezone.utc
            ).isoformat(),
        )

        item = asdict(example)

        profile = self.intelligence.analyze(
            name=example.name,
            description=example.description,
            code=example.code,
        )

        item["profile"] = profile.to_dict()

        items = self._load()
        items.append(item)
        self._save(items)

        return example

    def list(self) -> list[dict]:
        return self._load()
