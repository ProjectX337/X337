
class PreviewRegistry:

    def __init__(self):

        self.previews = {}


    def register(
        self,
        artifact,
        port,
        pid
    ):

        preview = {

            "name": artifact.name,

            "url":
                f"http://localhost:{port}",

            "port": port,

            "pid": pid,

            "status": "running"
        }


        self.previews[artifact.name] = preview


        return preview



    def get(
        self,
        name
    ):

        return self.previews.get(
            name
        )



    def remove(
        self,
        name
    ):

        if name in self.previews:

            del self.previews[name]

            return True


        return False



    def list(self):

        return list(
            self.previews.values()
        )

    
