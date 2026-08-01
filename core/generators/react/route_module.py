from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class RouteModule(BaseModule):
    """
    Generates application routes from UISpec and features.
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

        ui_spec = context.spec.ui_spec

        if ui_spec and ui_spec.page_models:
            pages.extend(
                ui_spec.page_models
            )

        if getattr(context.spec, "features", None):

            for feature in context.spec.features:

                if isinstance(feature, str):

                    pages.append(
                        {
                            "name": (
                                feature
                                .replace("_", " ")
                                .title()
                            ),
                            "route": (
                                "/" + feature
                                .lower()
                            ),
                            "feature": feature.lower(),
                        }
                    )

        for page in pages:

            if isinstance(page, dict):

                page_name = (
                    page["name"]
                    .replace(" ", "")
                )

                path = page["route"]

            else:

                page_name = page.name
                path = page.route

            if isinstance(page, dict):

                import_path = (
                    f'./features/{page_name.lower()}'
                )

            else:

                import_path = (
                    f'./pages/{page_name}'
                )

            routes.append(
                {
                    "path": path,
                    "page": page_name,
                    "import_path": import_path,
                }
            )

        context.builder.template(
            template="react/routes.tsx.j2",
            output="frontend/src/routes.tsx",
            language="typescript",
            routes=routes,
        )
