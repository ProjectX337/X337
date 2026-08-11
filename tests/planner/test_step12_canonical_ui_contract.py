from core.planner.project_planner import ProjectPlanner
from core.spec.project_spec import ProjectSpec
from core.spec.ui_spec import UISpec


PROMPT = """
Build an AI learning assistant with a modern web interface.
Users should be able to sign up, log in, chat with the AI,
search their learning history, and view a dashboard.
"""


def test_project_spec_has_canonical_ui_spec():
    result = ProjectPlanner().plan(PROMPT)

    assert isinstance(result, ProjectSpec)
    assert result.ui_spec is not None
    assert isinstance(result.ui_spec, UISpec)


def test_ui_spec_contains_canonical_page_models():
    result = ProjectPlanner().plan(PROMPT)
    ui = result.ui_spec

    assert ui.page_models

    for page in ui.page_models:
        assert page.name
        assert page.route
        assert page.components is not None


def test_ui_spec_contains_canonical_component_models():
    result = ProjectPlanner().plan(PROMPT)
    ui = result.ui_spec

    assert ui.component_models

    for component in ui.component_models:
        assert component.name
        assert component.component_type


def test_ui_spec_contains_design_system():
    result = ProjectPlanner().plan(PROMPT)
    ui = result.ui_spec

    assert ui.design_system is not None
    assert ui.design_system.theme
    assert ui.design_system.visual_style


def test_project_spec_does_not_duplicate_ui_models():
    result = ProjectPlanner().plan(PROMPT)

    assert not hasattr(result, "page_models")
    assert not hasattr(result, "component_models")
    assert not hasattr(result, "design_system")
