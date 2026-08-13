from core.planner.prompt_parser import PromptParser


def test_does_not_use_article_as_project_name():
    parsed = PromptParser().parse(
        "Build a project management application for a distributed engineering team"
    )

    assert parsed.project_name == "project-management"


def test_infers_name_from_product_description():
    parsed = PromptParser().parse(
        "Build a beautiful AI productivity dashboard"
    )

    assert parsed.project_name == (
        "beautiful-AI-productivity"
    )


def test_infers_dark_futuristic_dashboard():
    parsed = PromptParser().parse(
        "Create a dark futuristic SaaS dashboard"
    )

    assert parsed.project_name == (
        "dark-futuristic-SaaS"
    )


def test_infers_analytics_product():
    parsed = PromptParser().parse(
        "Build an analytics platform for a modern SaaS company"
    )

    assert parsed.project_name == "analytics"


def test_explicit_name_still_wins():
    parsed = PromptParser().parse(
        "Build an application called Nexus"
    )

    assert parsed.project_name == "Nexus"
