from core.capabilities import registry


def test_authentication_registered():
    capability = registry.get("authentication")

    assert capability is not None
    assert capability.name == "authentication"


def test_match_login():
    matches = registry.match("build a login page")

    assert matches
    assert matches[0].name == "authentication"
