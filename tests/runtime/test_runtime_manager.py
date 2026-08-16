import pytest

@pytest.fixture
def runtime_dependencies():
    process_manager = ProcessManager()

    preview_runtime = PreviewRuntime(
        process_manager
    )

    return (
        process_manager,
        preview_runtime,
    )



from pathlib import Path

from core.runtime.runtime_manager import RuntimeManager
from core.runtime.process_manager import ProcessManager
from core.preview.runtime import PreviewRuntime
from core.runtime.runtime_registry import RuntimeRegistry
from core.spec.project_spec import ProjectSpec


def test_runtime_manager_launch_preserves_project_spec(
    tmp_path,
    monkeypatch,
    runtime_dependencies,
):
    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    manager = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    )

    spec = ProjectSpec(
        name="Contract Test",
        path=str(
            tmp_path / "contract-test"
        ),
        framework="react",
    )

    monkeypatch.setattr(
        manager,
        "start_preview",
        lambda *args: {},
    )

    result = manager.launch(
        spec,
    )

    assert result["runtime"]["name"] == "Contract Test"
    assert result["runtime"]["slug"] == "contract-test"
    assert result["runtime"]["root_path"] == str(
        Path(spec.path)
    )
    assert result["runtime"]["status"] == "running"


def test_runtime_manager_start_preview_updates_registered_runtime(
    tmp_path,
    monkeypatch,
    runtime_dependencies,
):
    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    manager = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    )

    spec = ProjectSpec(
        name="Preview Contract",
        path=str(
            tmp_path / "preview-contract"
        ),
        framework="react",
    )

    runtime = manager.runtime_factory.create(
        spec=spec,
        root_path=Path(spec.path),
    )

    registry.register(runtime)

    preview = {
        "project": spec.slug,
        "status": "running",
        "port": 9100,
        "url": "http://127.0.0.1:9100",
    }

    monkeypatch.setattr(
        manager.preview_runtime,
        "start",
        lambda project_slug: preview,
    )

    result = manager.start_preview(
        spec.slug,
    )

    assert result == preview

    stored = registry.get(
        spec.project_name
    )

    assert stored["preview"] == preview


def test_runtime_registry_resolves_runtime_by_slug(
    tmp_path,
    runtime_dependencies,
):
    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    spec = ProjectSpec(
        name="Slug Contract",
        path=str(
            tmp_path / "slug-contract"
        ),
        framework="react",
    )

    runtime = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    ).runtime_factory.create(
        spec=spec,
        root_path=Path(spec.path),
    )

    registry.register(runtime)

    stored = registry.find_by_slug(
        spec.slug
    )

    assert stored is not None
    assert stored["slug"] == spec.slug
    assert stored["name"] == spec.project_name


def test_runtime_registry_update_preview_persists(
    tmp_path,
    runtime_dependencies,
):
    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    spec = ProjectSpec(
        name="Preview Persistence",
        path=str(
            tmp_path / "preview-persistence"
        ),
        framework="react",
    )

    runtime = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    ).runtime_factory.create(
        spec=spec,
        root_path=Path(spec.path),
    )

    registry.register(runtime)

    preview = {
        "project": spec.slug,
        "status": "running",
        "port": 9100,
        "url": "http://127.0.0.1:9100",
    }

    updated = registry.update_preview(
        spec.slug,
        preview,
    )

    assert updated["preview"] == preview

    reloaded = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    stored = reloaded.find_by_slug(
        spec.slug
    )

    assert stored["preview"] == preview


def test_runtime_monitor_persists_healthy_state(
    tmp_path,
    monkeypatch,
    runtime_dependencies,
):
    from core.runtime.runtime_monitor import RuntimeMonitor

    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    manager = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    )

    spec = ProjectSpec(
        name="Health Contract",
        path=str(
            tmp_path / "health-contract"
        ),
        framework="react",
    )

    runtime = manager.runtime_factory.create(
        spec=spec,
        root_path=Path(spec.path),
    )

    runtime.processes = {}

    registry.register(
        runtime
    )

    monitor = RuntimeMonitor(
        registry=registry
    )

    health = monitor.check(
        runtime
    )

    assert health["status"] == "healthy"
    assert "last_check" in health

    stored = registry.find_by_slug(
        spec.slug
    )

    assert stored["health"]["status"] == "healthy"
    assert "last_check" in stored["health"]


def test_runtime_monitor_persists_failed_state(
    tmp_path,
    monkeypatch,
    runtime_dependencies,
):
    from core.runtime.runtime_monitor import RuntimeMonitor

    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    manager = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    )

    spec = ProjectSpec(
        name="Failed Health Contract",
        path=str(
            tmp_path / "failed-health-contract"
        ),
        framework="react",
    )

    runtime = manager.runtime_factory.create(
        spec=spec,
        root_path=Path(spec.path),
    )

    from core.runtime.runtime_process import RuntimeProcess

    runtime.processes = {
        "999999999": RuntimeProcess(
            name="999999999",
            pid=999999999,
        )
    }

    registry.register(
        runtime
    )

    monitor = RuntimeMonitor(
        registry=registry
    )

    health = monitor.check(
        runtime
    )

    assert health["status"] == "failed"
    assert "last_check" in health

    stored = registry.find_by_slug(
        spec.slug
    )

    assert stored["health"]["status"] == "failed"
    assert "last_check" in stored["health"]


def test_runtime_registry_update_status_persists(
    tmp_path,
    runtime_dependencies,
):
    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    spec = ProjectSpec(
        name="Status Persistence",
        path=str(tmp_path / "status-persistence"),
        framework="react",
    )

    runtime = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    ).runtime_factory.create(
        spec=spec,
        root_path=Path(spec.path),
    )

    registry.register(runtime)

    updated = registry.update_status(
        spec.project_name,
        "generated",
    )

    assert updated["status"] == "generated"

    reloaded = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    stored = reloaded.get(
        spec.project_name
    )

    assert stored["status"] == "generated"


def test_runtime_manager_launch_persists_running_status(
    tmp_path,
    monkeypatch,
    runtime_dependencies,
):
    registry = RuntimeRegistry(
        storage_path=tmp_path / "runtimes.json"
    )

    manager = RuntimeManager(
        registry=registry,
        process_manager=runtime_dependencies[0],
        preview_runtime=runtime_dependencies[1],
    )

    spec = ProjectSpec(
        name="Running Status",
        path=str(tmp_path / "running-status"),
        framework="react",
    )

    monkeypatch.setattr(
        manager,
        "start_preview",
        lambda *args: {},
    )

    result = manager.launch(spec)

    assert result["runtime"]["status"] == "running"

    stored = registry.get(
        spec.project_name
    )

    assert stored["status"] == "running"
