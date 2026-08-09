from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined


class TemplateEngine:
    """
    Canonical Jinja2 template engine for X337.

    Responsibilities:
    - resolve repository-level templates
    - render templates with variables
    - expose template existence checks
    - preserve compatibility with template selection
    """

    def __init__(
        self,
        template_root: str | Path | None = None,
    ) -> None:

        if template_root is None:
            template_root = (
                Path(__file__).resolve().parents[2] / "templates"
            )

        self.template_root = Path(template_root).resolve()

        self.environment = Environment(
            loader=FileSystemLoader(str(self.template_root)),
            undefined=StrictUndefined,
            autoescape=False,
            keep_trailing_newline=True,
        )

        # Preserve the existing registry contract.
        try:
            from core.templates.template_registry import TemplateRegistry

            self.registry = TemplateRegistry()
        except Exception:
            self.registry = None

    # ============================================================
    # TEMPLATE LOOKUP
    # ============================================================

    def get_template(self, template: str):
        """
        Load a Jinja template by repository-relative path.

        Examples:
            react/page.tsx.j2
            react/component.tsx.j2
        """

        return self.environment.get_template(template)

    # ============================================================
    # EXISTENCE
    # ============================================================

    def exists(self, template: str) -> bool:
        """
        Return True when a template exists.
        """

        try:
            self.environment.get_template(template)
            return True
        except Exception:
            return False

    # ============================================================
    # RENDER
    # ============================================================

    def render(
        self,
        template: str,
        **variables: Any,
    ) -> str:
        """
        Render a repository-relative Jinja template.
        """

        jinja_template = self.get_template(template)

        return jinja_template.render(
            **variables
        )

    # ============================================================
    # TEMPLATE SELECTION
    # ============================================================

    def select_template(
        self,
        features,
    ):
        """
        Preserve the existing feature-based template selection API.
        """

        if self.registry is None:
            return None

        best_template = None
        best_score = 0

        for template in self.registry.list():

            score = 0

            for feature in features:
                if feature in template.features:
                    score += 1

            if score > best_score:
                best_score = score
                best_template = template

        return best_template
