import time
import psutil


class RuntimeMonitor:

    def __init__(
        self,
        registry,
    ):
        self.registry = registry

    def check(
        self,
        runtime
    ):

        alive = True

        for process in runtime.processes.values():

            try:

                p = psutil.Process(
                    process["pid"]
                )

                if not p.is_running():

                    alive = False

            except psutil.NoSuchProcess:

                alive = False

        health = {
            "status": (
                "healthy"
                if alive
                else "failed"
            ),
            "last_check": time.time(),
        }

        self.registry.update_health(
            runtime.slug,
            health,
        )

        return health
