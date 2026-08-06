from __future__ import annotations

from dataclasses import dataclass, field

from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_layout import UILayoutNode


@dataclass(slots=True)
class UIPage:

    name: str

    route: str

    layout: str = "default"

    components: list[UIComponent] = field(
        default_factory=list
    )

    composition: UILayoutNode | None = None

    metadata: dict = field(
        default_factory=dict
    )
