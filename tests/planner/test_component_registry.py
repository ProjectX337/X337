from core.knowledge.component_registry import COMPONENTS


def test_component_registry():

    assert "MetricCard" in COMPONENTS
    assert "Sidebar" in COMPONENTS

    assert len(
        COMPONENTS["MetricCard"].children
    ) > 0


if __name__ == "__main__":
    test_component_registry()
    print("✅ Component registry passed")
