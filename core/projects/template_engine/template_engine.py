from __future__ import annotations

from core.projects.specification.project_spec import ProjectSpec
from core.projects.template_engine.renderer import TemplateRenderer


class TemplateEngine:
    """
    High-level template engine for X337.

    Responsible for rendering every template for a framework
    into a dictionary of generated files.
    """

    def __init__(self):

        self.renderer = TemplateRenderer()

    # ==================================================

    def generate(
        self,
        spec: ProjectSpec,
    ) -> dict[str, str]:

        context = spec.as_dict()

        rendered = self.renderer.render_all(

            framework=spec.framework,

            context=context,

        )

        return rendered