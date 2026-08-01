from __future__ import annotations

from core.generators.modules.base_module import BaseModule


class FeaturePageModule(BaseModule):

    @property
    def name(self) -> str:
        return "feature_pages"

    def generate(self, context) -> None:

        for feature in context.spec.feature_models:

            for page in feature.pages:

                filename = (
                    page
                    .lower()
                    .replace(" ", "_")
                )

                context.builder.template(
                    template="react/feature/page.tsx.j2",
                    output=(
                        f"frontend/src/features/"
                        f"{feature.slug}/pages/"
                        f"{filename}.tsx"
                    ),
                    language="typescript",
                    page=page,
                    feature=feature.name,
                )
