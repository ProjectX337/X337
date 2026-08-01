from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class PackageModule(BaseModule):
    """
    Generates package.json and other
    package-management files.
    """

    @property
    def name(self) -> str:
        return "package"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        spec = context.spec

        project_name = (
            spec.parsed.project_name.strip()
            if spec.parsed.project_name
            else "x337-app"
        )

        context.builder.template(

            template="react/package.json.j2",

            output="frontend/package.json",

            language="json",

            project_name=project_name,

        )
