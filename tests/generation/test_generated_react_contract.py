from core.generators.default_registry import create_default_registry
from core.generators.generation_engine import GenerationEngine
from core.planner.project_planner import ProjectPlanner


def generate_project():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS"
    )

    return GenerationEngine(
        create_default_registry()
    ).generate(spec)


def test_generated_react_has_no_template_corruption():
    result = generate_project()

    for file in result.files:
        if not file.path.endswith((".tsx", ".ts", ".css")):
            continue

        content = file.content

        assert "```" not in content
        assert "\\<" not in content
        assert "\\>" not in content


def test_generated_app_is_valid_structure():
    result = generate_project()

    files = {
        file.path: file.content
        for file in result.files
    }

    app = files["frontend/src/App.tsx"]

    assert "RouterProvider" in app
    assert 'router from "./router"' in app
    assert "return <RouterProvider router={router} />;" in app


def test_generated_routes_have_elements():
    result = generate_project()

    routes = next(
        file.content
        for file in result.files
        if file.path == "frontend/src/routes.tsx"
    )

    assert "element: <" in routes
    assert "element: ," not in routes


def test_generated_pages_have_app_shell():
    result = generate_project()

    pages = [
        file
        for file in result.files
        if file.path.startswith("frontend/src/pages/")
    ]

    assert pages

    for page in pages:
        assert 'import AppShell from "../AppShell";' in page.content
        assert "<AppShell>" in page.content
        assert "</AppShell>" in page.content


def test_generated_components_have_real_jsx():
    result = generate_project()

    components = [
        file
        for file in result.files
        if file.path.startswith("frontend/src/components/")
    ]

    assert components

    for component in components:
        assert "<section" in component.content
        assert "</section>" in component.content
        assert "\\<section" not in component.content
