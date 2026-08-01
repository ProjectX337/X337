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

        for feature in context.spec.features:

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
