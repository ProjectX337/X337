class FileOperation:


    def __init__(
        self,
        path,
        content,
        operation="create"
    ):

        self.path = path

        self.content = content

        self.operation = operation



    def to_dict(
        self
    ):

        return {

            "path": self.path,

            "operation": self.operation,

            "size": len(self.content)

        }
