class RuntimeService:

    def __init__(
        self,
        runtime_manager,
        registry
    ):

        self.runtime = runtime_manager

        self.registry = registry



    #
    # Start runtime
    #
    def start(
        self,
        spec,
    ):

        return self.runtime.launch(
            spec,
        )




    #
    # Start preview
    #
    def start_preview(
        self,
        project_slug
    ):

        return self.runtime.start_preview(
            project_slug
        )

    #
    # Stop runtime
    #
    def stop(
        self,
        name
    ):

        return self.runtime.stop(
            name
        )



    #
    # Runtime status
    #
    def status(
        self,
        name
    ):

        return self.runtime.status(
            name
        )



    #
    # Runtime status mutation
    #
    def update_status(
        self,
        name,
        status,
    ):

        return self.registry.update_status(
            name,
            status,
        )


    #
    # Health state
    #
    def health(
        self,
        name
    ):

        runtime = self.registry.get(
            name
        )

        if runtime is None:
            return {
                "name": name,
                "healthy": False,
                "runtime": None,
            }

        health = runtime.get(
            "health",
            {}
        )

        return {

            "name": name,

            "healthy": (
                health.get(
                    "status"
                ) == "healthy"
            ),

            "runtime": runtime,

        }



    #
    # Restart runtime
    #
    def restart(
        self,
        spec,
    ):

        self.stop(
            spec.project_name
        )

        return self.start(
            spec,
        )



    #
    # Register runtime
    #
    def register(
        self,
        runtime
    ):

        return self.registry.register(
            runtime
        )


    #
    # Preview runtimes
    #
    def previews(
        self
    ):

        return [
            runtime
            for runtime in self.registry.list()
            if runtime.get("preview")
        ]



    #
    # Running runtimes
    #
    def list_running(
        self
    ):

        return self.registry.list()
