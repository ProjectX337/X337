from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.component_module import ComponentModule
from core.generators.react.page_naming import page_filename
from core.planner.project_planner import ProjectPlanner


def test_component_intelligence():

    spec = ProjectPlanner().plan(
        "Build an AI SaaS"
    )

    component = spec.ui_spec.component_models[0]

    component.props = {
        "variant": "string",
        "size": "string",
    }

    component.states = [
        "hover",
        "disabled",
    ]

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

    files = context.builder.result().files

    filename = page_filename(component.name)
    feature_slugs = component.metadata.get(
        "features",
        [],
    )

    if len(feature_slugs) == 1:
        expected = (
            "frontend/src/features/"
            f"{feature_slugs[0]}/components/"
            f"{filename}.tsx"
        )
    else:
        expected = (
            "frontend/src/components/"
            f"{filename}.tsx"
        )

    component_file = next(
        file
        for file in files
        if file.path == expected
    )

    assert "variant" in component_file.content
    assert "size" in component_file.content


if __name__ == "__main__":
    test_component_intelligence()
    print("Component intelligence passed")
