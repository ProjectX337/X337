class RuntimeController:
    """
    API-facing runtime orchestration boundary.

    FastAPI should communicate with runtime through
    this controller rather than directly touching services.
    """

    def __init__(self, service):
        self.service = service


    def start(self, artifact):
        return self.service.start(
            artifact
        )


    def stop(self, name):
        return self.service.stop(
            name
        )


    def status(self, name):
        return self.service.status(
            name
        )


    def running(self):
        return self.service.list_running()


    def previews(self):
        return self.service.previews()
