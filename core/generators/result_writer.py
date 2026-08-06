from pathlib import Path

from core.generators.generation_result import GenerationResult


class ResultWriter:

    def write(
        self,
        result: GenerationResult,
        root: str = ".",
    ):

        root_path = Path(root)

        for file in result.files:
            path = root_path / file.path

            path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            path.write_text(
                file.content
            )

        return root_path
