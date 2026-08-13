from core.planner.project_planner import ProjectPlanner


def _components(node):
    result = []

    if node.component is not None:
        result.append(node.component.name)

    for child in node.children:
        result.extend(_components(child))

    return result


def test_pages_do_not_share_unrelated_product_components():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication, AI assistant, analytics, dashboard, users, and search"
    )

    pages = {
        page.name: page
        for page in spec.ui_spec.page_models
    }

    landing = _components(pages["Landing"].composition)
    login = _components(pages["Login"].composition)
    ai = _components(pages["AI"].composition)

    assert "Sidebar" not in login
    assert "AuthForm" not in landing

    assert "ChatPanel" in ai
    assert "PromptBox" in ai


def test_page_composition_components_are_page_components():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS with authentication, AI assistant, analytics, dashboard, users, and search"
    )

    for page in spec.ui_spec.page_models:
        declared = {
            component.name
            for component in page.components
        }

        rendered = set(
            _components(page.composition)
        )

        assert rendered.issubset(declared), (
            f"{page.name}: composition contains "
            f"undeclared components: {rendered - declared}"
        )
