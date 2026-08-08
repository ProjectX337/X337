class RuntimeAPI:


    def __init__(
        self,
        runtime_controller
    ):

        self.controller = runtime_controller



    #
    # Start runtime
    #
    def start(
        self,
        artifact
    ):

        return self.controller.start(
            artifact
        )



    #
    # Stop runtime
    #
    def stop(
        self,
        name
    ):

        return self.controller.stop(
            name
        )



    #
    # Restart runtime
    #
    def restart(
        self,
        artifact
    ):

        return self.controller.restart(
            artifact
        )



    #
    # Runtime status
    #
    def status(
        self,
        name
    ):

        return self.controller.status(
            name
        )



    #
    # Runtime health
    #
    def health(
        self,
        name
    ):

        return self.controller.health(
            name
        )



    #
    # Running runtimes
    #
    def running(
        self
    ):

        return self.controller.list_running()



    #
    # Preview registry
    #
    def previews(
        self
    ):

        return self.controller.previews()