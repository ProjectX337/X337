from core.intelligence.reasoning.domain_rules import infer_domain
from core.intelligence.reasoning.workflow_rules import infer_workflows
from core.intelligence.reasoning.capability_rules import infer_capabilities


def test_learning_assistant_reasoning():

    text = (
        "Create an AI learning assistant "
        "for students"
    )

    assert infer_domain(text) == "education"

    assert (
        "student asks question"
        in infer_workflows(text)
    )

    assert (
        "ai"
        in infer_capabilities(text)
    )
