from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


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

        # Explicit features override planner defaults
        if context.spec.features:

            pages.extend(
                context.spec.features
            )

        # Structured UI pages
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

                name = page.name
                feature = page.name

            else:

                feature = page

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
