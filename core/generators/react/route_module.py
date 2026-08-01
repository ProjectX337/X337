from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class RouteModule(BaseModule):
    """
    Generates application routes from UISpec pages.
    """

    @property
    def name(self) -> str:
        return "routes"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        routes = []

        pages = []

        # Explicit features override planner defaults
        if context.spec.features:

            pages.extend(
                context.spec.features
            )

        # Structured pages
        elif (
            context.spec.ui_spec
            and getattr(
                context.spec.ui_spec,
                "page_models",
                None,
            )
        ):

            pages.extend(
                context.spec.ui_spec.page_models
            )

        elif context.spec.ui_spec:

            pages.extend(
                context.spec.ui_spec.pages
            )


        for page in pages:

            if hasattr(page, "name"):

                page_name = page.name

                path = (
                    page.route
                    .replace("/", "", 1)
                    if page.route != "/"
                    else ""
                )

                if path == "":
                    path = "/"

            else:

                page_name = (
                    page
                    .replace("_", " ")
                    .title()
                    .replace(" ", "")
                )

                path = (
                    page
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
