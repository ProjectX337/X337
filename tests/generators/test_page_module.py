from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.page_module import PageModule
from core.planner.project_planner import ProjectPlanner


def test_page_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    spec.features = [
        "authentication"
    ]

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

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert (
        "frontend/src/pages/Authentication.tsx"
        in paths
    )


if __name__ == "__main__":
    test_page_module()
    print("✅ PageModule passed")
