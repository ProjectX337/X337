from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.component_module import ComponentModule
from core.planner.project_planner import ProjectPlanner


def test_component_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="components",
            generator="components",
            description="Component generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    ComponentModule().generate(context)

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert (
        "frontend/src/components/Navbar.tsx"
        in paths
    )

    assert (
        "frontend/src/components/Button.tsx"
        in paths
    )

    assert (
        "frontend/src/components/Card.tsx"
        in paths
    )


if __name__ == "__main__":
    test_component_module()
    print("✅ ComponentModule passed")
