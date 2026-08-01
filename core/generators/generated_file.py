from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class GeneratedFile:
    """
    Represents a file generated in memory.

    The ProjectAssembler is responsible for writing
    GeneratedFiles to disk.
    """

    path: str

    content: str

    language: str = ""

    executable: bool = False

    metadata: dict[str, str] = field(
        default_factory=dict,
    )
