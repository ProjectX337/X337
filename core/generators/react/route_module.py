from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class RouteModule(BaseModule):
    """
    Generates application routes from generated pages.
    """

    @property
    def name(self) -> str:
        return "routes"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        routes = []

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

            page_name = (
                feature
                .replace("_", " ")
                .title()
                .replace(" ", "")
            )

            path = (
                feature
                .lower()
                .replace(" ", "-")
            )

            routes.append(
                {
                    "path": path,
                    "page": page_name,
                }
            )

        context.builder.template(
            template="react/routes.tsx.j2",
            output="frontend/src/routes.tsx",
            language="typescript",
            routes=routes,
        )
