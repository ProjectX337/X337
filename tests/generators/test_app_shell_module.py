from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.app_shell_module import AppShellModule
from core.planner.project_planner import ProjectPlanner


def test_app_shell_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="app_shell",
            generator="app_shell",
            description="Application shell",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    AppShellModule().generate(context)

    result = context.builder.result()

    file = result.files[0]

    assert file.path == "frontend/src/App.tsx"

    assert "RouterProvider" in file.content
    assert "./router" in file.content


if __name__ == "__main__":
    test_app_shell_module()
    print("✅ AppShellModule passed")
