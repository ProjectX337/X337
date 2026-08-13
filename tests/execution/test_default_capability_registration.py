from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)


def test_default_capabilities_registered():

    router = create_default_router()

    assert "modify_component" in router.handlers
    assert "update_route" in router.handlers
    assert "run_tests" in router.handlers
    assert "apply_feature_change" in router.handlers
