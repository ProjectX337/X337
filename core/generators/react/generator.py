from __future__ import annotations

from core.generators.base_generator import BaseGenerator
from core.generators.generator_context import GeneratorContext
from core.generators.generation_result import GenerationResult

from core.generators.react.package_module import PackageModule
from core.generators.react.config_module import ConfigModule
from core.generators.react.app_module import AppModule
from core.generators.react.style_module import StyleModule


class ReactGenerator(BaseGenerator):
    """
    Production React application generator.

    Responsible only for orchestration.
    Individual modules generate different
    parts of the project.
    """

    @property
    def name(self) -> str:
        return "react"

    def generate(
        self,
        context: GeneratorContext,
    ) -> GenerationResult:

        package = PackageModule()

        config = ConfigModule()

        app = AppModule()

        style = StyleModule()

        package.generate(context)

        config.generate(context)

        app.generate(context)

        style.generate(context)

        return context.builder.result()
