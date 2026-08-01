from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule
from core.generators.react.layout_renderer import LayoutRenderer


class PageModule(BaseModule):
    """
    Generates React pages from UISpec pages.
    """

    @property
    def name(self) -> str:
        return "pages"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        pages = []

        if (
            context.spec.ui_spec
            and getattr(
                context.spec.ui_spec,
                "page_models",
                None,
            )
        ):
            pages = context.spec.ui_spec.page_models

        for page in pages:

            context.builder.template(
                template="react/page.tsx.j2",
                output=f"frontend/src/pages/{page.name}.tsx",
                language="typescript",
                feature=page.name,
                page_name=page.name,
                route=page.route,
                components=page.components,
            composition=(
                LayoutRenderer().render(
                    page.composition
                )
                if page.composition
                else ""
            ),
            )
