from core.knowledge.architecture_registry import ARCHITECTURES


def test_registry():

    assert "SPA" in ARCHITECTURES
    assert "SSR" in ARCHITECTURES

    assert ARCHITECTURES["SPA"].routing == "client"


if __name__ == "__main__":
    test_registry()
    print("✅ Architecture registry passed")
