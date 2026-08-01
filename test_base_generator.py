from core.build.build_plan import BuildStep
from core.generators.base_generator import BaseGenerator
from core.generators.generated_file import GeneratedFile
from core.generators.generation_result import GenerationResult
from core.planner.project_planner import ProjectPlanner


class DummyGenerator(BaseGenerator):

    @property
    def name(self) -> str:

        return "dummy"

    def generate(
        self,
        spec,
        step,
    ):

        result = GenerationResult()

        result.add_file(

            GeneratedFile(

                path="dummy.txt",

                content="Hello from X337!",

                language="text",

            )

        )

        return result


planner = ProjectPlanner()

spec = planner.plan(
    "Build an AI SaaS."
)

generator = DummyGenerator()

step = BuildStep(
    name="Dummy",
    generator="dummy",
    description="Test",
    output_directory=".",
)

result = generator.generate(
    spec,
    step,
)

print(result)
