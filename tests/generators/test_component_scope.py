from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.component_module import ComponentModule
from core.generators.react.page_naming import page_filename
from core.planner.project_planner import ProjectPlanner


def _context(spec):
    return GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="components",
            generator="components",
            description="Component generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )


def test_feature_component_uses_canonical_feature_scope():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication"
    )

    auth = next(
        component
        for component in spec.ui_spec.component_models
        if component.name == "AuthForm"
    )

    assert auth.metadata.get("features") == [
        "authentication"
    ]

    context = _context(spec)
    ComponentModule().generate(context)

    paths = {
        file.path
        for file in context.builder.result().files
    }

    assert (
        "frontend/src/features/authentication/components/"
        f"{page_filename('AuthForm')}.tsx"
    ) in paths


def test_unowned_component_uses_global_scope():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS"
    )

    component = next(
        component
        for component in spec.ui_spec.component_models
        if not component.metadata.get("features")
    )

    context = _context(spec)
    ComponentModule().generate(context)

    paths = {
        file.path
        for file in context.builder.result().files
    }

    assert (
        "frontend/src/components/"
        f"{page_filename(component.name)}.tsx"
    ) in paths
