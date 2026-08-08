from dataclasses import dataclass, field



@dataclass
class ComponentBlueprint:

    name: str

    props: list[str] = field(
        default_factory=list
    )

    state: list[str] = field(
        default_factory=list
    )

    events: list[str] = field(
        default_factory=list
    )

    services: list[str] = field(
        default_factory=list
    )

    elements: list[str] = field(
        default_factory=list
    )