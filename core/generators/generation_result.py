from __future__ import annotations

from dataclasses import dataclass, field

from core.generators.generated_file import GeneratedFile


@dataclass(slots=True)
class GenerationResult:
    """
    Result returned by every generator.
    """

    files: list[GeneratedFile] = field(
        default_factory=list,
    )

    warnings: list[str] = field(
        default_factory=list,
    )

    notes: list[str] = field(
        default_factory=list,
    )

    def add_file(
        self,
        file: GeneratedFile,
    ) -> None:

        self.files.append(file)
