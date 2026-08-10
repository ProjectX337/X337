from core.planner.project_planner import ProjectPlanner
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.app_shell_module import AppShellModule
from core.build.build_plan import BuildStep


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

    assert file.path == "frontend/src/AppShell.tsx"
    assert "ReactNode" in file.content
    assert "children" in file.content
    assert "app-shell" in file.content
    assert "RouterProvider" not in file.content
