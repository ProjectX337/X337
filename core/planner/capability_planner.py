from __future__ import annotations

from core.capabilities.capability_registry import CapabilityRegistry
from core.planner.capability_match import CapabilityMatch
from core.planner.models import ParsedPrompt


class CapabilityPlanner:
    """
    Discovers and expands capabilities using the capability graph.
    """

    def __init__(self):
        self.registry = CapabilityRegistry()

    # ---------------------------------------------------------

    def plan(
        self,
        parsed: ParsedPrompt,
        candidates: list[str] | None = None,
    ) -> list[CapabilityMatch]:

        searchable = " ".join(
            [
                parsed.original,
                parsed.project_name,
                parsed.description,
                " ".join(parsed.keywords),
                parsed.project_type,
                parsed.style,
                parsed.domain,
            ]
        ).lower()

        scores: dict[str, int] = {}

        if candidates:
            for candidate in candidates:
                if self.registry.get(candidate):
                    scores[candidate] = 5


        for capability in self.registry.all():
            score = sum(
                keyword in searchable
                for keyword in capability.keywords
            )

            if score:
                scores[capability.name] = score

        expanded: dict[str, object] = {}
        visited: set[str] = set()

        def expand(capability):
            if capability.name in visited:
                return

            visited.add(capability.name)
            expanded[capability.name] = capability

            for dep in capability.depends_on:
                dep_cap = self.registry.get(dep)
                if dep_cap:
                    expand(dep_cap)

            for implied in capability.implies:
                imp_cap = self.registry.get(implied)
                if imp_cap:
                    expand(imp_cap)

        for name in scores:
            cap = self.registry.get(name)
            if cap:
                expand(cap)

        matches: list[CapabilityMatch] = []

        for capability in sorted(
            expanded.values(),
            key=lambda c: (
                -scores.get(c.name, 0),
                -c.priority,
                c.name,
            ),
        ):
            matches.append(
                CapabilityMatch(
                    capability=capability,
                    score=scores.get(capability.name, 1),
                    confidence=min(
                        1.0,
                        scores.get(capability.name, 1) / 5,
                    ),
                )
            )

        return matches
