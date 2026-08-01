from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class RouterModule(BaseModule):
    """
    Generates React Router configuration.
    """

    @property
    def name(self) -> str:
        return "router"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="react/router.tsx.j2",
            output="frontend/src/router.tsx",
            language="typescript",
        )
