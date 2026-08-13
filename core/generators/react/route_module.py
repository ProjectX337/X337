from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule
from core.generators.react.page_naming import page_filename


class RouteModule(BaseModule):
    """
    Generates application routes exclusively from canonical UIPage models.

    UISpec.page_models is the sole source of frontend page identity.
    Feature ownership is read from UIPage.metadata["feature"].
    """

    @property
    def name(self) -> str:
        return "routes"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:
        ui_spec = context.spec.ui_spec

        if not ui_spec:
            context.builder.template(
                template="react/routes.tsx.j2",
                output="frontend/src/routes.tsx",
                language="typescript",
                routes=[],
            )
            return

        routes = []

        for page in ui_spec.page_models:
            feature_slug = page.metadata.get("feature")

            filename = page_filename(page.name)
            component_name = page.name.replace(" ", "")

            if feature_slug:
                import_path = (
                    f"./features/{feature_slug}/pages/"
                    f"{filename}"
                )
            else:
                import_path = (
                    f"./pages/{page.name}"
                )

            routes.append(
                {
                    "path": page.route,
                    "page": component_name,
                    "import_path": import_path,
                }
            )

        context.builder.template(
            template="react/routes.tsx.j2",
            output="frontend/src/routes.tsx",
            language="typescript",
            routes=routes,
        )
