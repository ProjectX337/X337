from __future__ import annotations

from core.spec.project_spec import ProjectSpec
from core.projects.template_engine.template_engine import TemplateEngine


class ProjectGenerator:
    """
    X337 Project Generator v6

    Responsible only for generating files from templates.
    Architecture, planning, and dependency decisions are made
    before this stage.
    """

    def __init__(self):

        self.engine = TemplateEngine()

    # ==================================================

    def generate(
        self,
        spec: ProjectSpec,
    ) -> ProjectSpec:

        rendered_files = self.engine.generate(spec)

        for filename, content in rendered_files.items():
            spec.add_file(filename, content)

        spec.generated = True

        return spec