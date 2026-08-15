from core.runtime.runtime_controller import RuntimeController


class FakeService:

    def start(self, artifact):
        return "started"

    def stop(self, name):
        return "stopped"

    def restart(self, artifact):
        return "restarted"

    def status(self, name):
        return "status"

    def health(self, name):
        return "healthy"

    def list_running(self):
        return ["app"]

    def previews(self):
        return ["preview"]


def test_runtime_controller_boundary():

    controller = RuntimeController(
        FakeService()
    )

    assert controller.start(None) == "started"
    assert controller.stop("app") == "stopped"
    assert controller.restart(None) == "restarted"
    assert controller.status("app") == "status"
    assert controller.health("app") == "healthy"
    assert controller.list_running() == ["app"]
    assert controller.running() == ["app"]
    assert controller.previews() == ["preview"]
