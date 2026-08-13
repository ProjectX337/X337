from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.page_module import PageModule
from core.planner.project_planner import ProjectPlanner


def test_page_module_generates_feature_pages_from_ui_spec():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="pages",
            generator="pages",
            description="Page generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    PageModule().generate(context)

    paths = {
        file.path
        for file in context.builder.result().files
    }

    assert (
        "frontend/src/features/authentication/pages/login.tsx"
        in paths
    )

    assert (
        "frontend/src/features/authentication/pages/signup.tsx"
        in paths
    )


def test_page_module_generates_global_pages():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="pages",
            generator="pages",
            description="Page generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    PageModule().generate(context)

    paths = {
        file.path
        for file in context.builder.result().files
    }

    assert "frontend/src/pages/Landing.tsx" in paths
    assert "frontend/src/pages/Settings.tsx" in paths
