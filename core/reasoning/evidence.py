from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Evidence:

    source: str

    message: str

    weight: int
