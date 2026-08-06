from __future__ import annotations

from core.generators.modules.base_module import BaseModule


class FeatureComponentModule(BaseModule):

    @property
    def name(self) -> str:
        return "feature_components"

    def generate(self, context) -> None:

        for feature in context.spec.feature_models:

            for component in feature.components:

                filename = component.lower()

                context.builder.template(
                    template="react/feature/component.tsx.j2",
                    output=(
                        f"frontend/src/features/"
                        f"{feature.slug}/components/"
                        f"{filename}.tsx"
                    ),
                    language="typescript",
                    component=component,
                    feature=feature.name,
                    metadata=getattr(
                        component,
                        "metadata",
                        {},
                    ),
                )
