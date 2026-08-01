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

        features = context.spec.feature_models

        # Backward compatibility with legacy string features
        if not features:

            from core.spec.models.feature_spec import FeatureSpec

            features = [
                FeatureSpec(
                    name=f,
                    slug=(
                        f.lower()
                        .replace(" ", "_")
                    ),
                )
                for f in context.spec.features
            ]

        for feature in features:

            slug = feature.slug

            context.builder.template(
                template="react/feature/index.ts.j2",
                output=f"frontend/src/features/{slug}/index.ts",
                language="typescript",
                feature=feature.name,
            )
