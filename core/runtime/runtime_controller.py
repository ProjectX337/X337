class RuntimeController:


    def __init__(
        self,
        runtime_service
    ):

        self.runtime = runtime_service



    #
    # Start runtime
    #
    def start(
        self,
        artifact
    ):

        return self.runtime.start(
            artifact
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
    # Running runtimes
    #
    def list_running(
        self
    ):

        return self.runtime.list_running()



    #
    # Preview list
    #
    def previews(
        self
    ):

        return self.runtime.previews()



    #
    # Health check
    #
    def health(
        self,
        name
    ):

        return self.runtime.health(
            name
        )



    #
    # Restart runtime
    #
    def restart(
        self,
        artifact
    ):

        #
        # Stop existing instance
        #
        self.runtime.stop(
            artifact.name
        )


        #
        # Start fresh instance
        #
        return self.runtime.start(
            artifact
        )