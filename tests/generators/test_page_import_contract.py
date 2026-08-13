from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.generator import ReactGenerator
from core.planner.project_planner import ProjectPlanner


def test_generated_pages_use_canonical_component_locations():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication, AI assistant, analytics, dashboard, users, and search"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="react",
            generator="react",
            description="Full React generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    ReactGenerator().generate(context)

    files = {
        file.path: file
        for file in context.builder.result().files
    }

    landing = files[
        "frontend/src/pages/Landing.tsx"
    ]

    assert (
        '../features/ai/components/chat-panel'
        in landing.content
    )

    login = files[
        "frontend/src/features/authentication/pages/login.tsx"
    ]

    assert (
        '../components/auth-form'
        in login.content
    )
