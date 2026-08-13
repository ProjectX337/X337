from __future__ import annotations

from dataclasses import dataclass
from typing import List

from core.planner.architecture_requirements import (
    ArchitectureRequirements,
)
from core.planner.architecture_selector import ArchitectureCandidate


@dataclass
class ArchitectureStack:
    """
    Complete architecture selected for a project.

    Each field represents a system role.
    """

    frontend: str | None = None
    backend: str | None = None
    ai: str | None = None
    static_site: str | None = None
    scripting: str | None = None
    mobile: str | None = None
    desktop: str | None = None
    testing: str | None = None

    score: int = 0


class StackBuilder:
    """
    Builds a complete architecture stack from ranked
    candidates and canonical engineering requirements.
    """

    def build(
        self,
        candidates: List[ArchitectureCandidate],
        requirements: ArchitectureRequirements,
    ) -> ArchitectureStack:

        stack = ArchitectureStack()

        for candidate in candidates:

            architecture = candidate.architecture

            roles = {
                role.strip().lower()
                for role in architecture.roles
            }

            # -------------------------------------------------
            # Only fill roles explicitly required by the
            # architecture requirements.
            # -------------------------------------------------

            if (
                requirements.frontend
                and stack.frontend is None
                and "frontend" in roles
            ):
                stack.frontend = architecture.name
                stack.score += candidate.score
                continue

            if (
                requirements.backend
                and stack.backend is None
                and "backend" in roles
            ):
                stack.backend = architecture.name
                stack.score += candidate.score
                continue

            if (
                requirements.ai
                and stack.ai is None
                and "ai" in roles
            ):
                stack.ai = architecture.name
                stack.score += candidate.score
                continue

            if (
                requirements.static_site
                and stack.static_site is None
                and "static_site" in roles
            ):
                stack.static_site = architecture.name
                stack.score += candidate.score
                continue

            if (
                requirements.scripting
                and stack.scripting is None
                and "scripting" in roles
            ):
                stack.scripting = architecture.name
                stack.score += candidate.score
                continue

            if (
                requirements.mobile
                and stack.mobile is None
                and "mobile" in roles
            ):
                stack.mobile = architecture.name
                stack.score += candidate.score
                continue

            if (
                requirements.desktop
                and stack.desktop is None
                and "desktop" in roles
            ):
                stack.desktop = architecture.name
                stack.score += candidate.score
                continue

            if (
                requirements.testing
                and stack.testing is None
                and "testing" in roles
            ):
                stack.testing = architecture.name
                stack.score += candidate.score

        return stack
