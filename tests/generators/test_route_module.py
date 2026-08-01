from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.route_module import RouteModule
from core.planner.project_planner import ProjectPlanner


def test_route_module():

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
            name="routes",
            generator="routes",
            description="Route generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    RouteModule().generate(context)

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert (
        "frontend/src/routes.tsx"
        in paths
    )

    content = result.files[0].content

    assert "Authentication" in content
    assert "/authentication" in content


if __name__ == "__main__":
    test_route_module()
    print("✅ RouteModule passed")
