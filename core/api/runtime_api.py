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
        spec,
    ):

        return self.controller.start(
            spec,
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
        spec,
    ):

        return self.controller.restart(
            spec,
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