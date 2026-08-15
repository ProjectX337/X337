import json
from pathlib import Path


class RuntimeRegistry:

    def __init__(
        self,
        storage_path="workspace/runtime/project_runtimes.json"
    ):

        self.storage_path = Path(
            storage_path
        )

        self.runtimes = {}

        self._load()



    #
    # Load persisted runtimes
    #
    def _load(
        self
    ):

        if self.storage_path.exists():

            try:

                self.runtimes = json.loads(
                    self.storage_path.read_text()
                )

            except Exception:

                self.runtimes = {}

        else:

            self.runtimes = {}



    #
    # Save runtime state
    #
    def _save(
        self
    ):

        self.storage_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        self.storage_path.write_text(
            json.dumps(
                self.runtimes,
                indent=2
            )
        )



    #
    # Register project runtime
    #
    def register(
        self,
        runtime
    ):

        #
        # Prevent duplicate artifact runtimes
        #
        existing_id = None


        for runtime_id, existing in self.runtimes.items():

            if existing.get(
                "name"
            ) == runtime.name:

                existing_id = runtime_id
                break



        if existing_id:

            del self.runtimes[
                existing_id
            ]



        #
        # Store newest runtime
        #
        self.runtimes[
            runtime.id
        ] = runtime.to_dict()



        self._save()



    #
    # Find runtime by artifact name
    #
    def find_by_name(
        self,
        name
    ):

        for runtime in self.runtimes.values():

            if runtime.get(
                "name"
            ) == name:

                return runtime


        return None



    #
    # Get project runtime
    #
    def get(
        self,
        name
    ):

        return self.find_by_name(
            name
        )



    #
    # Remove runtime by name
    #
    def remove_by_name(
        self,
        name
    ):

        remove_runtime_ids = []


        for runtime_id, runtime in self.runtimes.items():

            if runtime.get(
                "name"
            ) == name:

                remove_runtime_ids.append(
                    runtime_id
                )



        for runtime_id in remove_runtime_ids:

            del self.runtimes[
                runtime_id
            ]



        self._save()



    #
    # Update runtime status
    #
    def update_status(
        self,
        name,
        status
    ):

        runtime = self.find_by_name(
            name
        )


        if runtime:

            runtime[
                "status"
            ] = status


            self._save()



    #
    # Update health information
    #
    def update_health(
        self,
        name,
        healthy
    ):

        runtime = self.find_by_name(
            name
        )


        if runtime:

            runtime[
                "health"
            ] = {

                "status":
                    "healthy"
                    if healthy
                    else "unhealthy"

            }


            self._save()



    #
    # List all runtimes
    #
    def list(
        self
    ):

        return list(
            self.runtimes.values()
        )
