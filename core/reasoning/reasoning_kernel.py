from __future__ import annotations

from collections import defaultdict

from core.reasoning.decision import Decision
from core.reasoning.evidence import Evidence


class ReasoningKernel:

    def __init__(self):

        self._scores = defaultdict(int)

        self._evidence = defaultdict(list)

        self._warnings = []

    # ---------------------------------------------------------

    def vote(

        self,

        candidate: str,

        *,

        weight: int,

        source: str,

        message: str,

    ):

        self._scores[candidate] += weight

        self._evidence[candidate].append(

            Evidence(

                source=source,

                message=message,

                weight=weight,

            )

        )

    # ---------------------------------------------------------

    def warn(self, message: str):

        self._warnings.append(message)

    # ---------------------------------------------------------

    def resolve(self) -> Decision:

        if not self._scores:

            return Decision(

                winner="",

                confidence=0.0,

                warnings=self._warnings,

            )

        ordered = sorted(

            self._scores.items(),

            key=lambda x: x[1],

            reverse=True,

        )

        winner, best_score = ordered[0]

        total = sum(self._scores.values())

        confidence = (

            best_score / total

            if total

            else 0.0

        )

        return Decision(

            winner=winner,

            confidence=confidence,

            evidence=[

                e.message

                for e in self._evidence[winner]

            ],

            alternatives=[

                (

                    name,

                    score / total,

                )

                for name, score in ordered[1:]

            ],

            warnings=self._warnings,

        )
