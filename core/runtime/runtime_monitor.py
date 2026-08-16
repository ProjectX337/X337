import time
import psutil

class RuntimeMonitor:

    def __init__(
        self,
        registry,
        process_manager=None,
    ):
        self.registry = registry

        self.process_manager = process_manager


    def check(
        self,
        runtime
    ):

        alive = True

        processes = {}

        if self.process_manager is not None:
            processes = (
                self.process_manager.list_runtime_processes()
            )

        if not processes:
            stored = self.registry.get(
                runtime.name
            )

            processes = {
                str(process.get("pid")): process
                for process in (
                    stored.get("processes", [])
                    if stored
                    else []
                )
            }

        for process in processes.values():

            try:

                pid = (
                    process.pid
                    if hasattr(process, "pid")
                    else process["pid"]
                )

                p = psutil.Process(
                    pid
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
