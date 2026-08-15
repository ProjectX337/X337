from __future__ import annotations

from core.generators.default_registry import create_default_registry
from core.generators.generation_engine import GenerationEngine
from core.generators.generation_result import GenerationResult
from core.spec.project_spec import ProjectSpec


class GenerationService:
    """
    Canonical application-generation boundary.

    All callers that need to generate a project should use
    this service rather than constructing generators directly.

    Responsibilities:

        ProjectSpec
            ↓
        GenerationEngine
            ↓
        BuildPlanner
            ↓
        GeneratorRegistry
            ↓
        Generators
            ↓
        GenerationResult
    """

    def __init__(
        self,
        engine: GenerationEngine | None = None,
    ) -> None:

        self.engine = (
            engine
            if engine is not None
            else GenerationEngine(
                create_default_registry()
            )
        )

    def generate(
        self,
        spec: ProjectSpec,
    ) -> GenerationResult:

        return self.engine.generate(
            spec
        )
