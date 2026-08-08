from dataclasses import dataclass, field
from typing import List


@dataclass
class LayoutStrategy:
    """
    AI-generated layout intelligence model.

    Determines how generated applications organize
    pages, sections, and user interaction flow.
    """

    page_type: str

    structure: List[str] = field(default_factory=list)

    layout_pattern: str = "dashboard"

    responsive_behavior: str = "adaptive"

    density: str = "balanced"

    navigation: str = "sidebar"

    user_flow: List[str] = field(default_factory=list)


    def to_dict(self):
        return self.__dict__
