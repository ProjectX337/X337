from __future__ import annotations

from jinja2 import Environment

from core.projects.template_engine.template_loader import TemplateLoader


class TemplateRenderer:
    """
    Renders Jinja templates using a ProjectSpec.

    Example:

        renderer.render(
            framework="fastapi",
            template="README.md.j2",
            context={"name": "InventoryAPI"}
        )
    """

    def __init__(self):

        self.loader = TemplateLoader()

        self.environment = Environment(

            autoescape=False,

            trim_blocks=True,

            lstrip_blocks=True,

        )

    # ==================================================

    def render(
        self,
        framework: str,
        template: str,
        context: dict,
    ) -> str:

        source = self.loader.load(

            framework,

            template,

        )

        jinja_template = self.environment.from_string(

            source

        )

        return jinja_template.render(

            **context

        )

    # ==================================================

    def render_all(
        self,
        framework: str,
        context: dict,
    ) -> dict[str, str]:

        rendered = {}

        templates = self.loader.list_templates(

            framework

        )

        for filename in templates:

            output_name = filename.removesuffix(".j2")

            rendered[output_name] = self.render(

                framework,

                filename,

                context,

            )

        return rendered