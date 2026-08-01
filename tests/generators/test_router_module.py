from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.router_module import RouterModule
from core.planner.project_planner import ProjectPlanner


def test_router_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="router",
            generator="router",
            description="Routing",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    RouterModule().generate(context)

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert "frontend/src/router.tsx" in paths


if __name__ == "__main__":
    test_router_module()
    print("✅ RouterModule passed")
