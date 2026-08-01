from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class AppShellModule(BaseModule):
    """
    Generates the React application shell.
    """

    @property
    def name(self) -> str:
        return "app_shell"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="react/app_shell.tsx.j2",
            output="frontend/src/AppShell.tsx",
            language="typescript",
        )

