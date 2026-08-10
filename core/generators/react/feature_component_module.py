from __future__ import annotations

import re

from core.generators.modules.base_module import BaseModule


def _component_filename(name: str) -> str:
    value = re.sub(
        r"(?<!^)(?=[A-Z])",
        "_",
        name,
    )

    value = re.sub(
        r"[^a-zA-Z0-9_]+",
        "_",
        value,
    )

    return value.lower().strip("_")


class FeatureComponentModule(BaseModule):

    @property
    def name(self) -> str:
        return "feature_components"

    def generate(self, context) -> None:

        for feature in context.spec.feature_models:

            for component in feature.components:

                if hasattr(component, "name"):
                    component_name = component.name
                    metadata = getattr(
                        component,
                        "metadata",
                        {},
                    )
                else:
                    component_name = str(component)
                    metadata = {}

                filename = _component_filename(
                    component_name
                )

                context.builder.template(
                    template="react/feature/component.tsx.j2",
                    output=(
                        f"frontend/src/features/"
                        f"{feature.slug}/components/"
                        f"{filename}.tsx"
                    ),
                    language="typescript",
                    component=component_name,
                    feature=feature.name,
                    metadata=metadata,
                )
