from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext
from core.generators.react.route_module import RouteModule
from core.planner.project_planner import ProjectPlanner
from core.spec.models.feature_spec import FeatureSpec


def test_route_module_uses_canonical_ui_pages():
    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    spec.feature_models = [
        FeatureSpec(
            name="Authentication",
            slug="authentication",
            pages=[
                "Login",
                "User Settings",
            ],
            routes=[
                "/login",
                "/user-settings",
            ],
        )
    ]

    # Simulate the canonical UIPlanner output.
    # RouteModule must consume UIPage models, not FeatureSpec.pages.
    spec.ui_spec.page_models = [
        page
        for page in spec.ui_spec.page_models
        if page.name not in {
            "AI",
            "Analytics",
            "Login",
            "Signup",
            "Users",
            "Dashboard",
        }
    ]

    from core.spec.models.ui_page import UIPage

    spec.ui_spec.page_models.extend(
        [
            UIPage(
                name="Login",
                route="/login",
                metadata={
                    "feature": "authentication",
                },
            ),
            UIPage(
                name="User Settings",
                route="/user-settings",
                metadata={
                    "feature": "authentication",
                },
            ),
        ]
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="routes",
            generator="routes",
            description="Route generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    RouteModule().generate(context)

    files = context.builder.result().files

    routes_file = next(
        file
        for file in files
        if file.path == "frontend/src/routes.tsx"
    )

    content = routes_file.content

    assert "/login" in content
    assert "/user-settings" in content
    assert "./features/authentication/pages/login" in content
    assert (
        "./features/authentication/pages/user-settings"
        in content
    )


def test_route_module_generates_global_pages():
    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    context = GeneratorContext(
        spec=spec,
        step=BuildStep(
            name="routes",
            generator="routes",
            description="Route generation",
            output_directory="frontend",
        ),
        builder=FileBuilder(),
    )

    RouteModule().generate(context)

    routes_file = next(
        file
        for file in context.builder.result().files
        if file.path == "frontend/src/routes.tsx"
    )

    assert './pages/Landing' in routes_file.content
    assert './pages/Settings' in routes_file.content
