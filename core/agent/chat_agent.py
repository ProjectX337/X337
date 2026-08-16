from __future__ import annotations

from pathlib import Path
import re

from core.agent.update_agent import UpdateAgent
from core.agent.response_formatter import ResponseFormatter
from core.memory.memory_manager import MemoryManager
from core.memory.project_memory import ProjectMemory
from core.memory.project_context_resolver import ProjectContextResolver
from core.memory.conversation_memory import ConversationMemory
from core.agent.router.intent_router import IntentRouter
from core.agent.change_engine import ChangeEngine
from core.generators.generation_service import GenerationService
from core.generators.result_writer import ResultWriter
from core.training.training_store import TrainingStore
from core.planner.project_planner import ProjectPlanner
from core.runtime.runtime_container import runtime_service


class ChatAgent:
    """
    Main X337 conversational agent.

    The chatbot is the conversational orchestration layer.
    Canonical application generation is delegated to
    GenerationService.
    """

    def __init__(self):

        self.project_planner = ProjectPlanner()

        self.change_engine = ChangeEngine()

        self.updater = UpdateAgent()

        self.generation_service = GenerationService()

        self.result_writer = ResultWriter()

        self.training_store = TrainingStore()

        self.output_root = Path(
            "workspace/generated"
        )

        self.formatter = ResponseFormatter()

        self.memory = MemoryManager()

        self.project_memory = ProjectMemory()


        self.runtime_service = runtime_service


        self.project_context = ProjectContextResolver()

        project = self.project_context.current()

        if project:
            self.updater.state.update(project)

        self.conversation = ConversationMemory()

        self.router = IntentRouter()

    def _safe_slug(self, value: str) -> str:
        value = value.strip().lower()

        value = re.sub(
            r"[^a-z0-9]+",
            "-",
            value,
        )

        return (
            value.strip("-")
            or "x337-app"
        )

    def _relevant_training_profiles(
        self,
        prompt: str,
    ) -> list[dict]:

        prompt_lower = prompt.lower()
        scored = []

        for example in self.training_store.list():

            profile = example.get(
                "profile",
                {},
            )

            score = 0

            for keyword in profile.get(
                "keywords",
                [],
            ):
                if keyword.lower() in prompt_lower:
                    score += 3

            for pattern in profile.get(
                "layout_patterns",
                [],
            ):
                if pattern.lower() in prompt_lower:
                    score += 2

            if profile.get("visual_style"):
                score += 1

            if score:
                scored.append(
                    (score, example)
                )

        scored.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [
            example
            for _, example in scored
        ]

    def _apply_training_profile(
        self,
        spec,
        profiles: list[dict],
    ) -> None:

        if not profiles:
            return

        design_system = getattr(
            spec,
            "design_system",
            None,
        )

        if design_system is None:

            ui_spec = getattr(
                spec,
                "ui_spec",
                None,
            )

            if ui_spec is not None:
                design_system = getattr(
                    ui_spec,
                    "design_system",
                    None,
                )

        if design_system is None:
            return

        metadata = getattr(
            design_system,
            "metadata",
            None,
        )

        if metadata is None:
            return

        metadata["training_profile"] = {
            "examples_used": len(profiles),
        }

    def _generate(self, message: str):

        spec = self.project_planner.plan(
            message
        )

        learned_examples = (
            self._relevant_training_profiles(
                message
            )
        )

        self._apply_training_profile(
            spec,
            learned_examples,
        )

        result = self.generation_service.generate(
            spec
        )

        slug = self._safe_slug(
            spec.project_name or message
        )

        output_root = (
            self.output_root / slug
        )

        output_root.mkdir(
            parents=True,
            exist_ok=True,
        )

        runtime = self.runtime_service.start(
            spec,
        )

        self.result_writer.write(
            result,
            root=str(output_root),
        )

        runtime.generation = {
            "files": len(result.files),
        }

        self.runtime_service.register(
            runtime
        )

        self.runtime_service.update_status(
            spec.project_name,
            "generated",
        )

        preview = self.runtime_service.start_preview(
            slug
        )

        self.project_memory.save_project(
            spec,
            {
                "status": "generated",
                "files": len(result.files),
            },
        )

        return {
            "spec": spec,
            "result": result,
            "slug": slug,
            "directory": str(output_root),
            "preview": preview,
        }

    def respond(
        self,
        message: str,
    ):

        intent = self.router.classify(message)

        context = self.project_context.enrich(message)

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

                generated = self._generate(
                    message
                )

                return {
                    "status": "updated",
                    "message": (
                        "X337 updated the application."
                    ),
                    "changes": [
                        change.feature
                        for change in state.changes
                    ],
                    "project": generated["slug"],
                    "directory": generated["directory"],
                    "files": len(
                        generated["result"].files
                    ),
                    "preview": generated["preview"],
                }

            return {
                "status": "updated",
                "message": (
                    "X337 applied the requested changes."
                ),
                "changes": [
                    change.feature
                    for change in state.changes
                ],
            }

        if intent == "repair":

            return {
                "status": "repair",
                "message": (
                    "Repair routing is available, "
                    "but no project repair was executed "
                    "through the chat endpoint yet."
                ),
            }

        generated = self._generate(
            message
        )

        spec = generated["spec"]
        result = generated["result"]
        preview = generated["preview"]

        return {
            "status": "generated",
            "message": (
                f"X337 generated {spec.project_name}."
            ),
            "project": generated["slug"],
            "directory": generated["directory"],
            "files": len(result.files),
            "pages": [
                page.name
                for page in spec.ui_spec.page_models
            ],
            "components": [
                component.name
                for component
                in spec.ui_spec.component_models
            ],
            "preview": preview,
        }
