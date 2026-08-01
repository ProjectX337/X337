from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class TypeScriptModule(BaseModule):
    """
    Generates TypeScript configuration files.
    """

    @property
    def name(self) -> str:
        return "typescript"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="react/tsconfig.json.j2",
            output="frontend/tsconfig.json",
            language="json",
        )

        context.builder.template(
            template="react/tsconfig.app.json.j2",
            output="frontend/tsconfig.app.json",
            language="json",
        )

        context.builder.template(
            template="react/tsconfig.node.json.j2",
            output="frontend/tsconfig.node.json",
            language="json",
        )
