from dataclasses import dataclass
from typing import List

from core.planner.models import Intent
from core.registry.architecture_registry import ArchitectureRegistry
from core.registry.architecture import Architecture


@dataclass
class ArchitectureCandidate:
    """
    Ranked architecture.
    """

    architecture: Architecture

    score: int


class ArchitectureSelector:
    """
    Chooses the best architecture(s)
    for an engineering intent.
    """

    def __init__(self):

        self.registry = ArchitectureRegistry()

    # -------------------------------------

    def select(
        self,
        intent: Intent,
    ) -> List[ArchitectureCandidate]:

        candidates = []

        for architecture in self.registry.all():

            score = self.score(
                architecture,
                intent,
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

    # -------------------------------------

    def best(
        self,
        intent: Intent,
    ) -> Architecture:

        return self.select(intent)[0].architecture

    # -------------------------------------

    def score(
        self,
        architecture: Architecture,
        intent: Intent,
    ) -> int:

        score = 0

        name = architecture.name.lower()

        keywords = {

            keyword.lower()

            for keyword in architecture.keywords
        }

        # -----------------------------
        # Frontend
        # -----------------------------

        if intent.frontend:

            if name == "react":

                score += 45

            elif name == "website":

                score += 35

        # -----------------------------
        # Backend
        # -----------------------------

        if intent.backend:

            if name == "fastapi":

                score += 45

            elif name == "python":

                score += 25

        # -----------------------------
        # Website
        # -----------------------------

        if intent.website:

            if name == "website":

                score += 30

        # -----------------------------
        # Dashboard
        # -----------------------------

        if intent.dashboard:

            if name == "react":

                score += 20

        # -----------------------------
        # AI
        # -----------------------------

        if intent.ai:

            if name == "ai_agent":

                score += 40

        # -----------------------------
        # Authentication
        # -----------------------------

        if intent.authentication:

            if name in {

                "fastapi",

                "react",

            }:

                score += 10

        # -----------------------------
        # Database
        # -----------------------------

        if intent.database:

            if name == "fastapi":

                score += 15

        # -----------------------------
        # Documentation
        # -----------------------------

        if intent.documentation:

            score += 5

        # -----------------------------
        # Testing
        # -----------------------------

        if intent.testing:

            if architecture.tester != "none":

                score += 5

        # -----------------------------
        # Keyword bonus
        # -----------------------------

        if intent.ai and "ai" in keywords:

            score += 10

        if intent.website and "website" in keywords:

            score += 5

        if intent.dashboard and "dashboard" in keywords:

            score += 5

        return score