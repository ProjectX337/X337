from dataclasses import dataclass, field


@dataclass
class ExecutionIntelligenceResult:
    """
    Output produced by execution intelligence analysis.
    """

    analysis: object | None = None

    evolution_plan: object | None = None

    signals: list = field(
        default_factory=list
    )

    confidence: float = 0.0
