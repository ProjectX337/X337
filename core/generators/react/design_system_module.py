from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class DesignSystemModule(BaseModule):
    """
    Generates frontend design tokens.
    """

    @property
    def name(self) -> str:
        return "design_system"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        if not context.spec.ui_spec:
            return

        design_system = (
            context.spec.ui_spec.design_system
        )

        context.builder.template(
            template="react/styles/tokens.css.j2",
            output="frontend/src/styles/tokens.css",
            language="css",
            colors=design_system.colors,
            spacing=design_system.spacing,
            typography=design_system.typography,
        )

        context.builder.template(
            template="react/styles/design_tokens.ts.j2",
            output="frontend/src/theme/design_tokens.ts",
            language="typescript",
            colors=design_system.colors,
            spacing=design_system.spacing,
            typography=design_system.typography,
        )
