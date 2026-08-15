from pathlib import Path

from core.runtime.project_runtime import ProjectRuntime
from core.spec.project_spec import ProjectSpec


def test_project_runtime_serializes_generation_state(
    tmp_path,
):
    spec = ProjectSpec(
        name="Generation Contract",
        path=str(tmp_path / "generation-contract"),
        framework="react",
    )

    runtime = ProjectRuntime(
        spec=spec,
        root_path=Path(spec.path),
    )

    runtime.generation = {
        "files": 7,
    }

    data = runtime.to_dict()

    assert data["generation"] == {
        "files": 7,
    }

    assert "artifacts" not in data


def test_project_runtime_starts_without_generation_state(
    tmp_path,
):
    spec = ProjectSpec(
        name="Empty Generation",
        path=str(tmp_path / "empty-generation"),
        framework="react",
    )

    runtime = ProjectRuntime(
        spec=spec,
        root_path=Path(spec.path),
    )

    assert runtime.generation == {}


def test_project_runtime_starts_without_health_state(
    tmp_path,
):
    spec = ProjectSpec(
        name="Empty Health",
        path=str(tmp_path / "empty-health"),
        framework="react",
    )

    runtime = ProjectRuntime(
        spec=spec,
        root_path=Path(spec.path),
    )

    assert runtime.health == {}

    data = runtime.to_dict()

    assert data["health"] == {}
