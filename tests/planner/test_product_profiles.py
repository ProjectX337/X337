from core.knowledge.product_profiles import (
    AI_SAAS,
    PORTFOLIO,
    ENTERPRISE,
    PRODUCT_PROFILES,
)


def test_registry():

    assert "ai_saas" in PRODUCT_PROFILES
    assert "portfolio" in PRODUCT_PROFILES
    assert "enterprise" in PRODUCT_PROFILES

    assert AI_SAAS.default_pages
    assert PORTFOLIO.default_pages
    assert ENTERPRISE.default_pages


if __name__ == "__main__":
    test_registry()
    print("✅ Product profile registry passed")
