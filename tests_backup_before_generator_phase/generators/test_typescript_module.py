from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.typescript_module import TypeScriptModule
from core.planner.project_planner import ProjectPlanner


def test_typescript_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="typescript",
            generator="typescript",
            description="TypeScript configuration",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    TypeScriptModule().generate(context)

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert "frontend/tsconfig.json" in paths
    assert "frontend/tsconfig.app.json" in paths
    assert "frontend/tsconfig.node.json" in paths


if __name__ == "__main__":
    test_typescript_module()
    print("✅ TypeScriptModule passed")
