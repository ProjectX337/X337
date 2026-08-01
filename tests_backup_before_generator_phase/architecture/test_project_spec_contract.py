from core.planner.models import Intent, ParsedPrompt, TechnologyPlan
from core.planner.stack_builder import ArchitectureStack
from core.spec.project_spec import ProjectSpec


def test_project_spec_contract():

    spec = ProjectSpec(
        prompt="Build an AI SaaS",

        parsed=ParsedPrompt(
            original="Build an AI SaaS",
            project_name="Nova",
            description="Demo project",
            keywords=[],
        ),

        intent=Intent(),

        architecture=None,

        capabilities=[],

        technologies=TechnologyPlan(),
    )

    assert spec.project_name == "Nova"
    assert spec.slug == "nova"
    assert spec.description == "Demo project"
    assert spec.keywords == []


if __name__ == "__main__":
    test_project_spec_contract()
    print("✅ ProjectSpec contract passed")
