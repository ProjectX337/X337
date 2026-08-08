class RuntimeRegistry:

    def __init__(self):
        self.apps = {}


    def register(
        self,
        artifact,
        runtime_info
    ):

        self.apps[artifact.name] = {
            "artifact": artifact,
            "runtime": runtime_info
        }


    def get(
        self,
        name
    ):

        return self.apps.get(name)


    def remove(
        self,
        name
    ):

        if name in self.apps:

            del self.apps[name]

            return True

        return False


    def list(self):

        return list(
            self.apps.values()
        )