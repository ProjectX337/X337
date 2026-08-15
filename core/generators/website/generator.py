from __future__ import annotations

from core.generators.base_generator import BaseGenerator
from core.generators.generator_context import GeneratorContext
from core.generators.generation_result import GenerationResult

from core.generators.website.html_module import HTMLModule
from core.generators.website.css_module import CSSModule
from core.generators.website.javascript_module import JavaScriptModule


class WebsiteGenerator(BaseGenerator):
    """
    Production static website generator.

    Generation pipeline:

        HTML
          ↓
        CSS
          ↓
        JavaScript
    """

    def __init__(self) -> None:
        self.modules = [
            HTMLModule(),
            CSSModule(),
            JavaScriptModule(),
        ]

    @property
    def name(self) -> str:
        return "website"

    def generate(
        self,
        context: GeneratorContext,
    ) -> GenerationResult:

        for module in self.modules:
            module.generate(context)

        return context.builder.result()
