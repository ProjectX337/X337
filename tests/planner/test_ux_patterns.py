from core.knowledge.ux_patterns import UX_PATTERNS


def test_patterns():

    assert "ai_dashboard" in UX_PATTERNS
    assert "portfolio" in UX_PATTERNS

    assert len(
        UX_PATTERNS["ai_dashboard"].sections
    ) > 0


if __name__ == "__main__":
    test_patterns()
    print("✅ UX patterns passed")
