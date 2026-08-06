from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class RouteModule(BaseModule):
    """
    Generates application routes from feature models
    and global UI pages.
    """

    @property
    def name(self) -> str:
        return "routes"


    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        routes = []

        feature_pages = set()

        #
        # Feature routes are canonical
        #

        for feature in getattr(
            context.spec,
            "feature_models",
            [],
        ):

            for page in feature.pages:

                filename = (
                    page
                    .lower()
                    .replace(" ", "")
                )

                component_name = page.replace(
                    " ",
                    ""
                )

                routes.append(
                    {
                        "path": (
                            f"/{feature.slug}/"
                            f"{filename}"
                        ),

                        "page": component_name,

                        "import_path": (
                            f"./features/"
                            f"{feature.slug}/pages/"
                            f"{filename}"
                        ),
                    }
                )

                feature_pages.add(page)


        #
        # Global UI pages only
        #

        ui_spec = context.spec.ui_spec

        if ui_spec:

            for page in ui_spec.page_models:

                if page.name in feature_pages:
                    continue


                routes.append(
                    {
                        "path": page.route,

                        "page": page.name,

                        "import_path": (
                            f"./pages/{page.name}"
                        ),
                    }
                )


        context.builder.template(
            template="react/routes.tsx.j2",
            output="frontend/src/routes.tsx",
            language="typescript",
            routes=routes,
        )
