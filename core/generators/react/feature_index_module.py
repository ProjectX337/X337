from __future__ import annotations

from core.generators.modules.base_module import BaseModule


class FeatureIndexModule(BaseModule):

    @property
    def name(self) -> str:
        return "feature_index"

    def generate(self, context) -> None:

        features = context.spec.feature_models

        if not features:
            features = context.spec.features

        for feature in features:

            if isinstance(feature, str):
                class FeatureProxy:
                    slug = feature
                    name = feature
                    pages = []

                feature = FeatureProxy()

            context.builder.template(
                template="react/feature/index.ts.j2",
                output=(
                    f"frontend/src/features/"
                    f"{feature.slug}/index.ts"
                ),
                language="typescript",
                feature=feature,
            )
