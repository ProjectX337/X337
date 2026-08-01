from __future__ import annotations

from core.generators.generated_file import GeneratedFile
from core.generators.generation_result import GenerationResult
from core.templates.template_engine import TemplateEngine


class FileBuilder:
    """
    Helper for constructing GenerationResults.

    Every generator should use FileBuilder instead
    of manually constructing GeneratedFiles.
    """

    def __init__(
        self,
        template_engine: TemplateEngine | None = None,
    ):

        self._result = GenerationResult()

        self._templates = (
            template_engine
            if template_engine is not None
            else TemplateEngine()
        )

    # ---------------------------------------------------------

    def add(
        self,
        *,
        path: str,
        content: str,
        language: str = "",
        executable: bool = False,
    ) -> None:

        self._result.add_file(

            GeneratedFile(

                path=path,

                content=content,

                language=language,

                executable=executable,

            )

        )

    # ---------------------------------------------------------

    def template(
        self,
        *,
        template: str,
        output: str,
        language: str = "",
        executable: bool = False,
        **variables,
    ) -> None:

        rendered = self._templates.render(
            template,
            **variables,
        )

        self.add(

            path=output,

            content=rendered,

            language=language,

            executable=executable,

        )

    # ---------------------------------------------------------

    def text(
        self,
        path: str,
        content: str,
    ) -> None:

        self.add(
            path=path,
            content=content,
            language="text",
        )

    # ---------------------------------------------------------

    def json(
        self,
        path: str,
        content: str,
    ) -> None:

        self.add(
            path=path,
            content=content,
            language="json",
        )

    # ---------------------------------------------------------

    def typescript(
        self,
        path: str,
        content: str,
    ) -> None:

        self.add(
            path=path,
            content=content,
            language="typescript",
        )

    # ---------------------------------------------------------

    def python(
        self,
        path: str,
        content: str,
    ) -> None:

        self.add(
            path=path,
            content=content,
            language="python",
        )

    # ---------------------------------------------------------

    def markdown(
        self,
        path: str,
        content: str,
    ) -> None:

        self.add(
            path=path,
            content=content,
            language="markdown",
        )

    # ---------------------------------------------------------

    def result(
        self,
    ) -> GenerationResult:

        return self._result
