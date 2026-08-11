from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.architecture_requirements import (
    ArchitectureRequirements,
)
from core.planner.stages.base_stage import PlanningStage


class ArchitectureRequirementsStage(PlanningStage):
    """
    Converts user intent and discovered capabilities
    into explicit engineering requirements.

    Capability requirements take precedence over the
    initial intent because capabilities represent the
    product behavior actually discovered by planning.
    """

    requires = {
        "intent",
        "capabilities",
    }

    provides = {
        "architecture_requirements",
    }

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        requirements = ArchitectureRequirements()

        # --------------------------------------------------
        # Intent-derived requirements
        # --------------------------------------------------

        intent = context.intent

        if intent is not None:

            if intent.frontend:
                requirements.require_role("frontend")

            if intent.backend:
                requirements.require_role("backend")

            if intent.ai:
                requirements.require_role("ai")

            if intent.website:
                requirements.require_role("static_site")

            if intent.testing:
                requirements.require_role("testing")

        # --------------------------------------------------
        # Capability-derived requirements
        # --------------------------------------------------

        for match in context.capabilities:

            capability = match.capability

            requirements.require_capability(
                capability.slug
            )

            for role in capability.required_roles:
                requirements.require_role(role)

            for endpoint in capability.api_endpoints:
                requirements.require_endpoint(endpoint)

            for technology in capability.technologies:
                requirements.require_technology(
                    technology
                )

        context.architecture_requirements = requirements
