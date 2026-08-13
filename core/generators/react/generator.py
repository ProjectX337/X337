from __future__ import annotations

from core.generators.base_generator import BaseGenerator
from core.generators.generator_context import GeneratorContext
from core.generators.generation_result import GenerationResult

from core.generators.react.package_module import PackageModule
from core.generators.react.vite_module import ViteModule
from core.generators.react.typescript_module import TypeScriptModule
from core.generators.react.app_module import AppModule
from core.generators.react.app_shell_module import AppShellModule
from core.generators.react.component_module import ComponentModule
from core.generators.react.feature_module import FeatureModule
from core.generators.react.page_module import PageModule
from core.generators.react.route_module import RouteModule
from core.generators.react.router_module import RouterModule
from core.generators.react.design_system_module import DesignSystemModule
from core.generators.react.style_module import StyleModule


class ReactGenerator(BaseGenerator):
    """
    Production React application generator.

    Generation pipeline:

        package
            ↓
        vite / typescript
            ↓
        app shell
            ↓
        components / features / pages
            ↓
        routes / router
            ↓
        design system / styles
    """

    def __init__(self) -> None:
        self.modules = [
            PackageModule(),
            ViteModule(),
            TypeScriptModule(),

            AppModule(),
            AppShellModule(),

            ComponentModule(),

            FeatureModule(),

            PageModule(),

            RouteModule(),
            RouterModule(),

            DesignSystemModule(),
            StyleModule(),
        ]

    @property
    def name(self) -> str:
        return "react"

    def generate(
        self,
        context: GeneratorContext,
    ) -> GenerationResult:

        if context.is_update:
            print(
                "React update mode:",
                context.changes,
            )

        for module in self.modules:
            module.generate(context)

        return context.builder.result()
