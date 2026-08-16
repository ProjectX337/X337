from dataclasses import dataclass, field


@dataclass
class ApplicationSnapshot:
    """
    Canonical understanding of a generated application.
    """

    project_name: str

    root_path: str

    framework: str = ""

    language: str = ""

    files: list[str] = field(
        default_factory=list
    )

    directories: list[str] = field(
        default_factory=list
    )

    pages: list[str] = field(
        default_factory=list
    )

    components: list[str] = field(
        default_factory=list
    )

    routes: list[str] = field(
        default_factory=list
    )

    dependencies: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )
