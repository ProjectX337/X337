from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.style_module import StyleModule
from core.planner.project_planner import ProjectPlanner


def test_style_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="style",
            generator="style",
            description="Global styles",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    StyleModule().generate(context)

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert "frontend/src/index.css" in paths


if __name__ == "__main__":
    test_style_module()
    print("✅ StyleModule passed")
