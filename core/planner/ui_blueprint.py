from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from core.spec.models.ui_page import UIPage


@dataclass
class UIBlueprint:
    """
    Transitional UI blueprint.

    UIPage is canonical and lives under core.spec.models.
    This class remains as a planner-level transport object while
    the planner pipeline is being consolidated.
    """

    application: str

    pages: list[UIPage] = field(default_factory=list)

    theme: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "application": self.application,
            "pages": [
                page.to_dict()
                for page in self.pages
            ],
            "theme": self.theme,
        }
