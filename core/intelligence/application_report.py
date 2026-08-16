from dataclasses import dataclass, field


@dataclass
class ApplicationReport:
    """
    Analysis result produced from an ApplicationSnapshot.
    """

    project_name: str

    framework: str = ""

    language: str = ""

    file_count: int = 0

    component_count: int = 0

    page_count: int = 0

    dependency_count: int = 0

    findings: list[str] = field(
        default_factory=list
    )

    recommendations: list[str] = field(
        default_factory=list
    )

    score: int = 0

    metadata: dict = field(
        default_factory=dict
    )
