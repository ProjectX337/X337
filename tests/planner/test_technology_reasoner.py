from core.knowledge.technology_reasoner import TechnologyReasoner
from core.knowledge.product_profiles import AI_SAAS
from core.knowledge.architecture_registry import SPA
from core.planner.models import Intent


def test_reasoner():

    reasoner = TechnologyReasoner()

    result = reasoner.infer(

        intent=Intent(ai=True),

        product_profile=AI_SAAS,

        architecture=SPA,

    )

    assert len(result) > 0

    assert result[0].score >= result[-1].score


if __name__ == "__main__":
    test_reasoner()
    print("✅ TechnologyReasoner passed")
