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
        artifact
    ):

        result = self.runtime.launch(
            artifact
        )

        return result




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
    # Health check
    #
    def health(
        self,
        name
    ):

        running = (
            self.runtime
            .process_manager
            .is_running(name)
        )

        return {

            "name": name,

            "healthy": running,

            "runtime": self.registry.get(name)

        }



    #
    # Restart runtime
    #
    def restart(
        self,
        artifact
    ):

        self.stop(
            artifact.name
        )

        return self.start(
            artifact
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
