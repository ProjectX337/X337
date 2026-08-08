from dataclasses import dataclass, field
from typing import List


@dataclass
class TemplateDefinition:

    name: str

    category: str

    pages: List[str] = field(
        default_factory=list
    )

    components: List[str] = field(
        default_factory=list
    )

    features: List[str] = field(
        default_factory=list
    )