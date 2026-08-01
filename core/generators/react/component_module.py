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

        components = []

        # Preferred: structured UI components
        if (
            context.spec.ui_spec
            and getattr(
                context.spec.ui_spec,
                "component_models",
                None,
            )
        ):

            components.extend(
                context.spec.ui_spec.component_models
            )

        # Existing UISpec support
        elif (
            context.spec.ui_spec
            and context.spec.ui_spec.components
        ):

            components.extend(
                context.spec.ui_spec.components
            )

            # Preserve legacy Header contract
            if "Header" not in components:

                components.insert(
                    0,
                    "Header",
                )

        # Safe fallback
        else:

            components.extend(
                [
                    "Header",
                    "Button",
                    "Card",
                ]
            )


        for component in components:

            if hasattr(component, "name"):

                name = component.name

            else:

                name = component


            context.builder.template(
                template="react/component.tsx.j2",
                output=f"frontend/src/components/{name}.tsx",
                language="typescript",
                component=name,
            )
