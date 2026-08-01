from core.planner.stages.base_stage import PlanningStage
from core.planner.planning_context import PlanningContext


class DummyStage(PlanningStage):

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        print("Stage executed")

        print(context.prompt)


context = PlanningContext(
    prompt="Build an AI SaaS"
)

DummyStage().run(context)
