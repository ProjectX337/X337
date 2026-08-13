from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.component_module import ComponentModule
from core.generators.react.page_naming import page_filename
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

    paths = {
        file.path
        for file in result.files
    }

    expected = set()

    for component in spec.ui_spec.component_models:
        features = component.metadata.get(
            "features",
            [],
        )

        filename = page_filename(
            component.name
        )

        if len(features) == 1:
            expected.add(
                f"frontend/src/features/"
                f"{features[0]}/components/"
                f"{filename}.tsx"
            )
        else:
            expected.add(
                f"frontend/src/components/"
                f"{filename}.tsx"
            )

    assert expected.issubset(paths)


if __name__ == "__main__":
    test_component_module()
    print("ComponentModule passed")
