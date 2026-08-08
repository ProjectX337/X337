from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Artifact:

    name: str

    artifact_type: str

    path: str

    framework: Optional[str] = None

    install_commands: List[str] = field(default_factory=list)

    run_commands: List[str] = field(default_factory=list)

    preview_port: Optional[int] = None

    status: str = "created"
