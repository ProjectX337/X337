from __future__ import annotations

import re

from core.generators.modules.base_module import BaseModule


def _page_filename(name: str) -> str:
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


class FeaturePageModule(BaseModule):

    @property
    def name(self) -> str:
        return "feature_pages"

    def generate(self, context) -> None:

        for feature in context.spec.feature_models:

            for page in feature.pages:

                page_name = (
                    page.name
                    if hasattr(page, "name")
                    else str(page)
                )

                filename = _page_filename(
                    page_name
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
                    page_name=page_name,
                    feature=feature.name,
                )
