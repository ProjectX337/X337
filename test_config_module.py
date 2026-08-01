from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.config_module import ConfigModule
from core.planner.project_planner import ProjectPlanner

planner = ProjectPlanner()

spec = planner.plan(
    "Build an AI SaaS called Nova."
)

context = GeneratorContext(
    spec=spec,
    step=BuildStep(
        name="React",
        generator="react",
        description="Frontend",
        output_directory="frontend",
    ),
    builder=FileBuilder(),
)

ConfigModule().generate(context)

result = context.builder.result()

for file in result.files:
    print(file.path)
