from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.feature_module import FeatureModule
from core.planner.project_planner import ProjectPlanner


def test_feature_module():

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
            name="features",
            generator="features",
            description="Feature generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    FeatureModule().generate(context)

    result = context.builder.result()

    paths = [
        file.path
        for file in result.files
    ]

    assert (
        "frontend/src/features/authentication/index.ts"
        in paths
    )


if __name__ == "__main__":
    test_feature_module()
    print("✅ FeatureModule passed")
