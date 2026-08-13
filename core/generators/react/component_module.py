from __future__ import annotations

import re

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule
from core.generators.react.component_strategy import component_template_for


def _component_filename(name: str) -> str:
    value = re.sub(
        r"([A-Z]+)([A-Z][a-z])",
        r"\1 \2",
        str(name).strip(),
    )

    value = re.sub(
        r"([a-z0-9])([A-Z])",
        r"\1 \2",
        value,
    )

    value = re.sub(
        r"[^a-zA-Z0-9]+",
        "-",
        value,
    )

    return value.strip("-").lower()


class ComponentModule(BaseModule):
    """
    Generates canonical UIComponent models.

    UIComponent.metadata["features"] determines scope:

        [] / missing
            frontend/src/components/

        ["authentication"]
            frontend/src/features/authentication/components/
    """

    @property
    def name(self) -> str:
        return "components"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:
        if not context.spec.ui_spec:
            return

        for component in context.spec.ui_spec.component_models:
            feature_slugs = sorted(
                set(
                    component.metadata.get(
                        "features",
                        [],
                    )
                )
            )

            filename = _component_filename(
                component.name
            )

            if len(feature_slugs) == 1:
                output = (
                    f"frontend/src/features/"
                    f"{feature_slugs[0]}/components/"
                    f"{filename}.tsx"
                )

                template = component_template_for(component)

                variables = {
                    "component": component,
                    "feature": feature_slugs[0],
                    "metadata": component.metadata,
                }

            elif not feature_slugs:
                output = (
                    f"frontend/src/components/"
                    f"{filename}.tsx"
                )

                template = component_template_for(component)

                variables = {
                    "component": component,
                    "metadata": component.metadata,
                }

            else:
                raise ValueError(
                    "Component belongs to multiple features "
                    f"and has no shared component policy: "
                    f"{component.name}: {feature_slugs}"
                )

            context.builder.template(
                template=template,
                output=output,
                language="typescript",
                **variables,
            )
