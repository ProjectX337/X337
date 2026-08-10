from core.generators.default_registry import create_default_registry
from core.generators.generation_engine import GenerationEngine
from core.planner.project_planner import ProjectPlanner


def test_react_generation_baseline():
    spec = ProjectPlanner().plan(
        "Build an AI SaaS"
    )

    result = GenerationEngine(
        create_default_registry()
    ).generate(spec)

    files = {
        file.path: file.content
        for file in result.files
    }

    required_files = [
        "frontend/package.json",
        "frontend/index.html",
        "frontend/src/main.tsx",
        "frontend/src/App.tsx",
        "frontend/src/AppShell.tsx",
        "frontend/src/router.tsx",
        "frontend/src/routes.tsx",
    ]

    for path in required_files:
        assert path in files, f"Missing generated file: {path}"

    main = files["frontend/src/main.tsx"]
    app = files["frontend/src/App.tsx"]
    shell = files["frontend/src/AppShell.tsx"]

    # main.tsx
    assert "<React.StrictMode>" in main
    assert "</React.StrictMode>" in main
    assert "<App />" in main

    # App.tsx
    assert "RouterProvider" in app
    assert "router={router}" in app
    assert "return <RouterProvider router={router} />;" in app

    # AppShell.tsx
    assert "return ;" not in shell

    # No shell escaping may leak into generated TSX.
    for path in required_files:
        if path.endswith((".tsx", ".ts")):
            content = files[path]
            assert r"\<" not in content, f"Escaped JSX in {path}"
            assert r"\</" not in content, f"Escaped JSX in {path}"

    # No empty React returns.
    for path in required_files:
        if path.endswith(".tsx"):
            assert "return ;" not in files[path], (
                f"Empty return in {path}"
            )

    assert 'id="root"' in files[
        "frontend/index.html"
    ]

    assert "createBrowserRouter" in files[
        "frontend/src/router.tsx"
    ]

    assert "RouteObject[]" in files[
        "frontend/src/routes.tsx"
    ]

    for route in [
        "Landing",
        "Dashboard",
        "Settings",
        "Billing",
        "API",
    ]:
        assert route in files[
            "frontend/src/routes.tsx"
        ]
