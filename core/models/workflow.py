from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class WorkflowStep:

    name: str

    capability: str

    status: str = "Pending"

    assigned_agent: Optional[str] = None

    result: Optional[object] = None



@dataclass
class Workflow:

    name: str

    steps: List[WorkflowStep] = field(
        default_factory=list
    )

    status: str = "Created"