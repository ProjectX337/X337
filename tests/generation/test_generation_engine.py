from core.planner.project_planner import ProjectPlanner

from core.generators.generation_engine import GenerationEngine
from core.generators.default_registry import create_default_registry


def test_generation_engine():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    engine = GenerationEngine(
        create_default_registry()
    )

    result = engine.generate(
        spec
    )

    paths = [
        file.path
        for file in result.files
    ]

    assert len(paths) > 0

    assert any(
        "package.json" in path
        for path in paths
    )
