class RuntimeController:
    """
    API-facing runtime orchestration boundary.

    FastAPI communicates with runtime through this controller
    rather than directly touching RuntimeService.
    """

    def __init__(self, service):
        self.service = service

    def start(self, artifact):
        return self.service.start(artifact)

    def stop(self, name):
        return self.service.stop(name)

    def restart(self, artifact):
        return self.service.restart(artifact)

    def status(self, name):
        return self.service.status(name)

    def health(self, name):
        return self.service.health(name)

    def list_running(self):
        return self.service.list_running()

    def running(self):
        return self.list_running()

    def previews(self):
        return self.service.previews()
