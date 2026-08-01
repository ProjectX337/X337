from core.capabilities.capability import Capability
from core.planner.capability_match import CapabilityMatch

authentication = Capability(
    name="authentication",
)

match = CapabilityMatch(
    capability=authentication,
    score=8,
    confidence=0.95,
)

print(match)
