from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class ConfigModule(BaseModule):
    """
    Generates the React/Vite configuration files.
    """

    @property
    def name(self) -> str:
        return "config"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        builder = context.builder

        project_name = context.spec.project_name

        builder.template(
            template="react/vite.config.ts.j2",
            output="frontend/vite.config.ts",
            language="typescript",
            project_name=project_name,
        )

        builder.template(
            template="react/tsconfig.json.j2",
            output="frontend/tsconfig.json",
            language="json",
            project_name=project_name,
        )

        builder.template(
            template="react/tsconfig.app.json.j2",
            output="frontend/tsconfig.app.json",
            language="json",
            project_name=project_name,
        )

        builder.template(
            template="react/tsconfig.node.json.j2",
            output="frontend/tsconfig.node.json",
            language="json",
            project_name=project_name,
        )
