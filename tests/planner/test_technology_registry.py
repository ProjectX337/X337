from core.knowledge.technology_registry import TECHNOLOGIES


def test_registry():

    assert "nextjs" in TECHNOLOGIES
    assert "react" in TECHNOLOGIES
    assert "fastapi" in TECHNOLOGIES

    assert "SSR" in TECHNOLOGIES["nextjs"].strengths


if __name__ == "__main__":
    test_registry()
    print("✅ Technology registry passed")
