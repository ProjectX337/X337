from __future__ import annotations

from pathlib import Path


class TemplateLoader:
    """
    Loads Jinja templates from disk.

    Example:

        loader.load(
            "fastapi",
            "app.py.j2"
        )
    """

    def __init__(
        self,
        template_root: str | Path | None = None,
    ):

        if template_root is None:

            template_root = (
                Path(__file__)
                .parent.parent
                / "templates"
            )

        self.template_root = Path(
            template_root
        )

    # ==================================================

    def framework_directory(
        self,
        framework: str,
    ) -> Path:

        directory = (
            self.template_root
            / framework.lower()
        )

        if not directory.exists():

            raise FileNotFoundError(

                f"No templates for framework '{framework}'."

            )

        return directory

    # ==================================================

    def load(
        self,
        framework: str,
        filename: str,
    ) -> str:

        template = (
            self.framework_directory(
                framework
            )
            / filename
        )

        if not template.exists():

            raise FileNotFoundError(

                f"Template not found: {template}"

            )

        return template.read_text(
            encoding="utf-8"
        )

    # ==================================================

    def list_templates(
        self,
        framework: str,
    ) -> list[str]:

        directory = self.framework_directory(
            framework
        )

        return sorted(

            file.name

            for file in directory.glob("*.j2")

        )