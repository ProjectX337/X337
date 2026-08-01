from __future__ import annotations

from abc import ABC, abstractmethod

from core.generators.generation_result import GenerationResult
from core.generators.generator_context import GeneratorContext


class BaseGenerator(ABC):
    """
    Base class for all generators.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        context: GeneratorContext,
    ) -> GenerationResult:
        raise NotImplementedError
