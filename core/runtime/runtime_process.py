from dataclasses import dataclass, field
import time


@dataclass
class RuntimeProcess:

    name: str

    pid: int

    port: int | None = None

    process_type: str = "runtime"

    status: str = "running"

    created_at: float = field(
        default_factory=time.time
    )


    def to_dict(self) -> dict:

        return {
            "name": self.name,
            "pid": self.pid,
            "port": self.port,
            "process_type": self.process_type,
            "status": self.status,
            "created_at": self.created_at,
        }
