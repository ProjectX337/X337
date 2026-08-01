from __future__ import annotations

from core.ai.planner_agent import PlannerAgent
from core.agent.update_agent import UpdateAgent
from core.agent.autonomous_agent import AutonomousAgent
from core.agent.factory.agent_factory import create_autonomous_agent
from core.agent.context_builder import create_generator_context
from core.agent.response_formatter import ResponseFormatter
from core.memory.memory_manager import MemoryManager
from core.memory.project_memory import ProjectMemory
from core.memory.project_context_resolver import ProjectContextResolver
from core.memory.conversation_memory import ConversationMemory
from core.agent.router.intent_router import IntentRouter


class ChatAgent:
    """
    Main X337 conversational agent.
    """

    def __init__(self):

        self.planner = PlannerAgent()

        self.updater = UpdateAgent()

        self.builder = create_autonomous_agent()

        self.repair_agent = (
            self.builder.executor.tools["repair"].agent
        )

        self.formatter = ResponseFormatter()

        self.memory = MemoryManager()

        self.project_memory = ProjectMemory()

        self.project_context = ProjectContextResolver()

        project = self.project_context.current()

        if project:
            self.updater.state.update(
                project
            )

        self.conversation = ConversationMemory()

        self.router = IntentRouter()


    def respond(
        self,
        message: str,
    ):

        intent = self.router.classify(
            message
        )

        context = self.project_context.enrich(
            message
        )

        self.conversation.add_turn(
            message,
            intent,
        )


        if intent == "modify":

            state = self.updater.apply(
                message,
                context,
            )


            self.memory.remember(
                "last_change",
                [
                    change.to_dict()
                    for change in state.changes
                ],
            )


            if state.project:

                build_context = create_generator_context(
                    state.project,
                    changes=state.changes,
                    project_state=state,
                )


                result = self.builder.build(
                    build_context
                )


                self.project_memory.save_project(
                    state.project,
                    result,
                )


                return (
                    "Updated project.\n\n"
                    "Changes:\n"
                    + "\n".join(
                        f"✓ {c.feature}"
                        for c in state.changes
                    )
                    + "\n\n"
                    "Regeneration:\n"
                    f"✓ React application regenerated\n"
                    f"✓ {result['generated']['files']} files created\n"
                )


            return (
                "Updated project with: "
                + ", ".join(
                    change.feature
                    for change in state.changes
                )
            )


        if intent == "repair":

            return self.repair_agent.run_loop()



        spec = self.planner.build(
            message
        )

        context = create_generator_context(
            spec,
            changes=self.updater.state.changes,
            project_state=self.updater.state,
        )

        result = self.builder.build(
            context
        )


        self.project_memory.save_project(
            spec,
            result,
        )

        return self.formatter.format(
            spec.project_name,
            result,
        )
