from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Ranking:

    name: str

    score: int
