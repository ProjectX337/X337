from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.app_module import AppModule
from core.planner.project_planner import ProjectPlanner


def test_app_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="app",
            generator="app",
            description="React application",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    AppModule().generate(context)

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert "frontend/index.html" in paths
    assert "frontend/src/main.tsx" in paths
    assert "frontend/src/App.tsx" in paths


if __name__ == "__main__":
    test_app_module()
    print("✅ AppModule passed")
