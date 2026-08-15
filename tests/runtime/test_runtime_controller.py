from core.runtime.runtime_controller import RuntimeController


class FakeService:

    def start(self, artifact):
        return "started"

    def stop(self, name):
        return "stopped"

    def status(self, name):
        return "status"

    def list_running(self):
        return []

    def previews(self):
        return []


def test_runtime_controller_boundary():

    controller = RuntimeController(
        FakeService()
    )

    assert controller.start(None) == "started"
    assert controller.stop("app") == "stopped"
    assert controller.status("app") == "status"
    assert controller.running() == []
    assert controller.previews() == []
