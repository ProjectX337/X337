from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class PageModule(BaseModule):
    """
    Generates React pages from project features.
    """

    @property
    def name(self) -> str:
        return "pages"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        pages = (
            context.spec.features
            if context.spec.features
            else (
                context.spec.ui_spec.pages
                if context.spec.ui_spec
                else []
            )
        )

        for feature in pages:

            name = (
                feature
                .replace("_", " ")
                .title()
                .replace(" ", "")
            )

            context.builder.template(
                template="react/page.tsx.j2",
                output=f"frontend/src/pages/{name}.tsx",
                language="typescript",
                feature=feature,
                page_name=name,
            )
