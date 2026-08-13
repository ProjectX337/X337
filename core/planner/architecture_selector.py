from __future__ import annotations

from dataclasses import dataclass
from typing import List

from core.planner.architecture_requirements import (
    ArchitectureRequirements,
)
from core.registry.architecture import Architecture
from core.registry.architecture_registry import ArchitectureRegistry


@dataclass
class ArchitectureCandidate:
    """
    Ranked architecture candidate.
    """

    architecture: Architecture
    score: int


class ArchitectureSelector:
    """
    Chooses architectures for canonical engineering
    requirements.

    The selector does not interpret user intent directly.
    Intent has already been converted into
    ArchitectureRequirements by the planning pipeline.
    """

    def __init__(self) -> None:
        self.registry = ArchitectureRegistry()

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def select(
        self,
        requirements: ArchitectureRequirements,
    ) -> List[ArchitectureCandidate]:

        candidates: list[ArchitectureCandidate] = []

        for architecture in self.registry.all():

            score = self.score(
                architecture,
                requirements,
            )

            candidates.append(
                ArchitectureCandidate(
                    architecture=architecture,
                    score=score,
                )
            )

        candidates.sort(
            key=lambda candidate: candidate.score,
            reverse=True,
        )

        return candidates

    # ---------------------------------------------------------
    # Best
    # ---------------------------------------------------------

    def best(
        self,
        requirements: ArchitectureRequirements,
    ) -> Architecture:

        candidates = self.select(requirements)

        if not candidates:
            raise RuntimeError(
                "Architecture registry contains no architectures."
            )

        return candidates[0].architecture

    # ---------------------------------------------------------
    # Scoring
    # ---------------------------------------------------------

    def score(
        self,
        architecture: Architecture,
        requirements: ArchitectureRequirements,
    ) -> int:

        score = 0

        roles = {
            role.strip().lower()
            for role in architecture.roles
        }

        keywords = {
            keyword.strip().lower()
            for keyword in architecture.keywords
        }

        # -----------------------------------------------------
        # Required roles
        # -----------------------------------------------------

        for required_role in requirements.required_roles:

            role = required_role.strip().lower()

            if role in roles:
                score += 50

        # -----------------------------------------------------
        # Required capabilities
        #
        # Architecture metadata can declare compatible
        # capabilities through metadata["capabilities"].
        # -----------------------------------------------------

        architecture_capabilities = {
            str(value).strip().lower()
            for value in architecture.metadata.get(
                "capabilities",
                [],
            )
        }

        for capability in requirements.required_capabilities:

            if capability.lower() in architecture_capabilities:
                score += 25

        # -----------------------------------------------------
        # Required technologies
        #
        # Architecture metadata may declare supported
        # technologies through metadata["technologies"].
        # -----------------------------------------------------

        architecture_technologies = {
            str(value).strip().lower()
            for value in architecture.metadata.get(
                "technologies",
                [],
            )
        }

        architecture_technologies.update(
            str(value).strip().lower()
            for value in architecture.technology_defaults.keys()
        )

        for technology in requirements.required_technologies:

            if technology.lower() in architecture_technologies:
                score += 20

        # -----------------------------------------------------
        # Endpoint requirements
        #
        # Architectures with backend/API roles are favored
        # when capabilities introduced API endpoints.
        # -----------------------------------------------------

        if requirements.required_endpoints:

            if "backend" in roles:
                score += 20

            if "api" in keywords:
                score += 10

        # -----------------------------------------------------
        # Keyword compatibility
        # -----------------------------------------------------

        for capability in requirements.required_capabilities:

            if capability.lower() in keywords:
                score += 10

        # -----------------------------------------------------
        # Testing
        # -----------------------------------------------------

        if requirements.testing:

            if architecture.tester != "none":
                score += 10

        # -----------------------------------------------------
        # Small keyword compatibility bonuses
        # -----------------------------------------------------

        if requirements.ai and "ai" in keywords:
            score += 10

        if requirements.static_site and "website" in keywords:
            score += 10

        if requirements.frontend and "frontend" in keywords:
            score += 5

        if requirements.backend and "backend" in keywords:
            score += 5

        return score
