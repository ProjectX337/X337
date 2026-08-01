from __future__ import annotations

from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import StrictUndefined


class TemplateEngine:
    """
    Loads and renders Jinja2 templates.

    All project generators share one template engine.
    """

    def __init__(
        self,
        template_directory: str = "templates",
    ):

        self.directory = Path(template_directory)

        self.environment = Environment(

            loader=FileSystemLoader(
                self.directory,
            ),

            autoescape=False,

            trim_blocks=True,

            lstrip_blocks=True,

            undefined=StrictUndefined,

        )

    # ---------------------------------------------------------

    def render(
        self,
        template: str,
        **variables,
    ) -> str:

        return (

            self.environment

            .get_template(template)

            .render(**variables)

        )
