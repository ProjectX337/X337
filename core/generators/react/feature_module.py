from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class FeatureModule(BaseModule):
    """
    Generates feature folders from ProjectSpec features.
    """

    @property
    def name(self) -> str:
        return "features"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        for feature in context.spec.features:

            slug = (
                feature
                .lower()
                .replace(" ", "_")
            )

            context.builder.template(
                template="react/feature/index.ts.j2",
                output=f"frontend/src/features/{slug}/index.ts",
                language="typescript",
                feature=feature,
            )
