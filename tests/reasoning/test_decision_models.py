from core.reasoning.decision import Decision
from core.reasoning.evidence import Evidence
from core.reasoning.ranking import Ranking


def test_models():

    decision = Decision(
        winner="SPA",
        confidence=0.95,
    )

    evidence = Evidence(
        source="Intent",
        message="Dashboard detected",
        weight=5,
    )

    ranking = Ranking(
        name="SPA",
        score=10,
    )

    assert decision.winner == "SPA"
    assert evidence.weight == 5
    assert ranking.score == 10


if __name__ == "__main__":
    test_models()
    print("✅ Reasoning models passed")
