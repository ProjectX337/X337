from core.graph.evolution.models import (
    GraphChangeSet,
    ImpactReport,
)

from core.graph.evolution.evolution_strategy import (
    EvolutionStrategy,
)


def test_strategy_generates_actions():

    plan = EvolutionStrategy().generate(
        GraphChangeSet(
            added_nodes=[
                "component.mfa"
            ]
        ),
        ImpactReport(
            affected_nodes=[
                "page.login"
            ],
            severity="medium",
        ),
    )

    assert (
        "implement new architecture surface: component.mfa"
        in plan.actions
    )

    assert plan.priority == "normal"
