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

        if hasattr(runtime, "processes"):
            self.runtimes[
                runtime.id
            ]["processes"] = [
                process.to_dict()
                for process in runtime.processes.values()
            ]



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
    # Get project runtime by name
    #
    def get(
        self,
        name
    ):

        return self.find_by_name(
            name
        )


    #
    # Find project runtime by slug
    #
    def find_by_slug(
        self,
        slug
    ):

        for runtime in self.runtimes.values():

            if runtime.get(
                "slug"
            ) == slug:

                return runtime


        return None


    #
    # Update preview state
    #
    def update_preview(
        self,
        slug,
        preview
    ):

        runtime = self.find_by_slug(
            slug
        )

        if runtime is None:
            return None

        runtime[
            "preview"
        ] = preview

        self._save()

        return runtime



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

            return runtime

        return None



    #
    # Update runtime process state
    #
    def update_processes(
        self,
        slug,
        processes,
    ):

        runtime = self.find_by_slug(
            slug
        )

        if runtime is None:
            return None

        runtime[
            "processes"
        ] = [
            process.to_dict()
            for process in processes.values()
        ]

        self._save()

        return runtime



    #
    # Update health information
    #
    def update_health(
        self,
        slug,
        health
    ):

        runtime = self.find_by_slug(
            slug
        )

        if runtime is None:
            return None

        runtime[
            "health"
        ] = dict(
            health
        )

        self._save()

        return runtime



    #
    # List all runtimes
    #
    def list(
        self
    ):

        return list(
            self.runtimes.values()
        )
