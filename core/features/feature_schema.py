from dataclasses import dataclass, field



@dataclass
class FeatureBlueprint:


    name: str


    category: str


    pages: list[str] = field(
        default_factory=list
    )


    components: list[str] = field(
        default_factory=list
    )


    services: list[str] = field(
        default_factory=list
    )


    ai_capabilities: list[str] = field(
        default_factory=list
    )


    analytics: list[str] = field(
        default_factory=list
    )