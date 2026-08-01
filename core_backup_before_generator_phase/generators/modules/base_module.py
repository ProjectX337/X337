from __future__ import annotations

from abc import ABC, abstractmethod

from core.generators.generator_context import GeneratorContext


class BaseModule(ABC):
    """
    Base class for all generation modules.

    Modules are responsible for generating
    a logical portion of a project.

    Examples:

    - PackageModule
    - ConfigModule
    - AppModule
    - StyleModule
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable module name.
        """
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        context: GeneratorContext,
    ) -> None:
        """
        Generate this module's files.

        Modules should add files to
        context.builder.
        """
        raise NotImplementedError
