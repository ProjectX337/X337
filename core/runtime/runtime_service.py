class RuntimeService:

    def __init__(
        self,
        runtime_manager,
    ):

        self.runtime = runtime_manager



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

        return self.runtime.update_status(
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

        runtime = self.runtime.status(
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

        return self.runtime.register(
            runtime
        )


    #
    # Preview runtimes
    #
    def previews(
        self
    ):

        return self.runtime.previews()



    #
    # Running runtimes
    #
    def list_running(
        self
    ):

        return self.runtime.list_running()
