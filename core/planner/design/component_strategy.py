from dataclasses import dataclass, field
from typing import List


@dataclass
class ComponentStrategy:

    component_type: str

    components: List[str] = field(
        default_factory=list
    )

    interaction_level: str = "standard"

    animation_behavior: str = "subtle"

    accessibility: str = "WCAG"

    responsive_behavior: str = "adaptive"

    state_management: str = "local"

    def to_dict(self):
        return self.__dict__
