from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.component_module import ComponentModule
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

    component_file = [
        f
        for f in files
        if f.path.endswith(f"{component.name}.tsx")
    ][0]

    assert "variant" in component_file.content
    assert "size" in component_file.content


if __name__ == "__main__":
    test_component_intelligence()
    print("✅ Component intelligence passed")
