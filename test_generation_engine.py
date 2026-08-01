from core.generators.base_generator import BaseGenerator
from core.generators.generated_file import GeneratedFile
from core.generators.generation_engine import GenerationEngine
from core.generators.generation_result import GenerationResult
from core.generators.generator_registry import GeneratorRegistry
from core.planner.project_planner import ProjectPlanner


class DummyGenerator(BaseGenerator):

    def __init__(self, generator_name: str):

        self._name = generator_name

    @property
    def name(self):

        return self._name

    def generate(
        self,
        spec,
        step,
    ):

        result = GenerationResult()

        result.add_file(

            GeneratedFile(

                path=f"{step.output_directory}/generated.txt",

                content=f"{step.generator} generated this",

                language="text",

            )

        )

        return result


planner = ProjectPlanner()

spec = planner.plan(
    """
    Build an AI SaaS with authentication,
    PostgreSQL,
    dashboards,
    and AI assistants.
    """
)

registry = GeneratorRegistry()

registry.register(DummyGenerator("react"))
registry.register(DummyGenerator("fastapi"))
registry.register(DummyGenerator("ai_agent"))
registry.register(DummyGenerator("python"))

engine = GenerationEngine(registry)

result = engine.generate(spec)

print()

print("Generated Files")

print("=" * 40)

for file in result.files:

    print(file.path)
