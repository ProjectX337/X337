from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class ComponentModule(BaseModule):
    """
    Generates reusable React components.
    """

    @property
    def name(self) -> str:
        return "components"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        components = (
            context.spec.ui_spec.component_models
            if context.spec.ui_spec
            else []
        )

        for component in components:

            context.builder.template(
                template="react/component.tsx.j2",
                output=f"frontend/src/components/{component.name}.tsx",
                language="typescript",
                component=component.name,
            )
