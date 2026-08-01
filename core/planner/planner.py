from __future__ import annotations

from core.planner.architecture_selector import ArchitectureSelector
from core.planner.intent_classifier import IntentClassifier
from core.planner.models import PlanningResult
from core.planner.prompt_parser import PromptParser
from core.planner.stack_builder import StackBuilder
from core.planner.technology_resolver import TechnologyResolver


class Planner:
    """
    High-level planning pipeline.

    This is the single public entry point for all
    planning operations inside X337.
    """

    def __init__(self):

        self.parser = PromptParser()

        self.intent_classifier = IntentClassifier()

        self.architecture_selector = ArchitectureSelector()

        self.stack_builder = StackBuilder()

        self.technology_resolver = TechnologyResolver()

    # ---------------------------------------------------------

    def plan(
        self,
        prompt: str,
    ) -> PlanningResult:

        parsed = self.parser.parse(prompt)

        intent = self.intent_classifier.classify(parsed)

        candidates = self.architecture_selector.select(intent)

        stack = self.stack_builder.build(
            candidates,
            intent,
        )

        technologies = self.technology_resolver.resolve(
            stack,
        )

        architecture = " + ".join(
            filter(
                None,
                [
                    stack.frontend,
                    stack.backend,
                    stack.ai,
                    stack.static_site,
                    stack.mobile,
                    stack.desktop,
                ],
            )
        )

        framework = stack.backend or stack.frontend or ""

        return PlanningResult(
            parsed=parsed,
            intent=intent,
            architecture=architecture,
            framework=framework,
            technologies=technologies,
        )
