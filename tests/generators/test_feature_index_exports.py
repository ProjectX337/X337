from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.feature_module import FeatureModule
from core.planner.project_planner import ProjectPlanner


def test_feature_index_exports_only_canonical_feature_pages():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication, AI assistant, analytics, dashboard, users, and search"
    )

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

    files = {
        file.path: file
        for file in context.builder.result().files
    }

    authentication = files[
        "frontend/src/features/authentication/index.ts"
    ]

    dashboard = files[
        "frontend/src/features/dashboard/index.ts"
    ]

    assert './pages/login' in authentication.content
    assert './pages/signup' in authentication.content

    # Dashboard's FeatureSpec references Dashboard, but the canonical
    # UIPage is a global page, so the feature index must not export it.
    assert './pages/dashboard' not in dashboard.content
    assert dashboard.content.strip() == "export {};"
