from core.graph.evolution.models import (
    GraphChangeSet,
    ImpactReport,
    EvolutionPlan,
)


def test_evolution_models():

    change = GraphChangeSet(
        added_nodes=["component.mfa"]
    )

    impact = ImpactReport(
        affected_nodes=["page.login"]
    )

    plan = EvolutionPlan(
        actions=[
            "add MFA component"
        ]
    )

    assert change.added_nodes == [
        "component.mfa"
    ]

    assert impact.affected_nodes == [
        "page.login"
    ]

    assert plan.actions[0] == (
        "add MFA component"
    )
