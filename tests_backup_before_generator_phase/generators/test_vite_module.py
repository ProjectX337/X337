from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.vite_module import ViteModule
from core.planner.project_planner import ProjectPlanner


def test_vite_module():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="React",
            generator="react",
            description="Frontend",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    ViteModule().generate(context)

    result = context.builder.result()

    assert len(result.files) == 1

    assert result.files[0].path == "frontend/vite.config.ts"


if __name__ == "__main__":
    test_vite_module()
    print("✅ ViteModule passed")
