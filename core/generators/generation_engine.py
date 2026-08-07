from __future__ import annotations

from core.build.build_planner import BuildPlanner
from core.generators.file_builder import FileBuilder
from core.generators.generation_result import GenerationResult
from core.generators.generator_context import GeneratorContext
from core.generators.generator_registry import GeneratorRegistry
from core.spec.project_spec import ProjectSpec


class GenerationEngine:
    """
    Coordinates project generation.

    Responsibilities:
    - Create a BuildPlan
    - Create GeneratorContext
    - Execute generators
    - Merge GenerationResults
    """

    def __init__(
        self,
        registry: GeneratorRegistry,
    ):

        self.registry = registry

        self.build_planner = BuildPlanner()

    # ---------------------------------------------------------

    def generate(
        self,
        spec: ProjectSpec,
    ) -> GenerationResult:

        build_plan = self.build_planner.build(
            spec,
        )

        final_result = GenerationResult()

        for step in build_plan.ordered_steps():

            generator = self.registry.get(
                step.generator,
            )

            context = GeneratorContext(
                spec=spec,
                step=step,
                builder=FileBuilder(),
            )

        try:
            result = generator.generate(
                context,
            )
        except Exception:
            import traceback

            print("\n" + "=" * 80)
            print(f"GENERATOR FAILED: {generator.__class__.__name__}")
            traceback.print_exc()
            print("=" * 80 + "\n")
            raise

            final_result.files.extend(
                result.files,
            )

            final_result.warnings.extend(
                result.warnings,
            )

            final_result.notes.extend(
                result.notes,
            )

        return final_result
