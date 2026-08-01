from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.package_module import PackageModule
from core.planner.project_planner import ProjectPlanner
from core.build.build_plan import BuildStep

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

PackageModule().generate(context)

result = context.builder.result()

for file in result.files:

    print()

    print(file.path)

    print("=" * 50)

    print(file.content)
