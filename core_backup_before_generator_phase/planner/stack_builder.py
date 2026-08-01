from dataclasses import dataclass
from typing import List

from core.planner.architecture_selector import ArchitectureCandidate
from core.planner.models import Intent


# ============================================================
# Architecture Stack
# ============================================================

@dataclass
class ArchitectureStack:
    """
    Complete architecture selected for a project.

    Each field represents a role in the final system.
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


# ============================================================
# Stack Builder
# ============================================================

class StackBuilder:
    """
    Builds a complete architecture stack
    from ranked architectures.
    """

    def build(
        self,
        candidates: List[ArchitectureCandidate],
        intent: Intent,
    ) -> ArchitectureStack:

        stack = ArchitectureStack()

        for candidate in candidates:

            architecture = candidate.architecture

            roles = set(architecture.roles)

            # --------------------------------------------------
            # Frontend
            # --------------------------------------------------

            if (
                intent.frontend
                and stack.frontend is None
                and "frontend" in roles
            ):

                stack.frontend = architecture.name
                stack.score += candidate.score
                continue

            # --------------------------------------------------
            # Backend
            # --------------------------------------------------

            if (
                intent.backend
                and stack.backend is None
                and "backend" in roles
            ):

                stack.backend = architecture.name
                stack.score += candidate.score
                continue

            # --------------------------------------------------
            # AI
            # --------------------------------------------------

            if (
                intent.ai
                and stack.ai is None
                and "ai" in roles
            ):

                stack.ai = architecture.name
                stack.score += candidate.score
                continue

            # --------------------------------------------------
            # Static Website
            # --------------------------------------------------

            if (
                intent.website
                and stack.static_site is None
                and "static_site" in roles
            ):

                stack.static_site = architecture.name
                stack.score += candidate.score
                continue

            # --------------------------------------------------
            # Scripting
            # --------------------------------------------------

            if (
                stack.scripting is None
                and "scripting" in roles
            ):

                stack.scripting = architecture.name
                stack.score += candidate.score // 2
                continue

            # --------------------------------------------------
            # Mobile
            # --------------------------------------------------

            if (
                stack.mobile is None
                and "mobile" in roles
            ):

                stack.mobile = architecture.name
                stack.score += candidate.score
                continue

            # --------------------------------------------------
            # Desktop
            # --------------------------------------------------

            if (
                stack.desktop is None
                and "desktop" in roles
            ):

                stack.desktop = architecture.name
                stack.score += candidate.score
                continue

            # --------------------------------------------------
            # Testing
            # --------------------------------------------------

            if (
                stack.testing is None
                and "testing" in roles
            ):

                stack.testing = architecture.name

        return stack