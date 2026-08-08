from pathlib import Path


class AppExplorer:
    """
    Inspects generated X337 applications.
    Provides file discovery and source access.
    """


    def __init__(
        self,
        root="workspace/generated"
    ):

        self.root = Path(root)



    def inspect(
        self,
        project_name
    ):

        project_path = (
            self.root /
            project_name
        )


        if not project_path.exists():

            return {
                "status": "error",
                "message": "Project not found"
            }



        files = []


        for file in project_path.rglob("*"):

            if file.is_file():

                files.append({

                    "path":
                        str(
                            file.relative_to(
                                project_path
                            )
                        ),

                    "type":
                        self.detect_type(
                            file
                        )

                })


        return {

            "project":
                project_name,

            "files":
                files,

            "count":
                len(files)

        }



    def read_file(
        self,
        project_name,
        relative_path
    ):

        file = (
            self.root /
            project_name /
            relative_path
        )


        if not file.exists():

            return None


        return file.read_text()



    def detect_type(
        self,
        file
    ):

        path = str(file)


        if "/components/" in path:

            return "component"


        if "/pages/" in path:

            return "page"


        if "/services/" in path:

            return "service"


        if file.name.endswith(
            (".tsx", ".ts", ".jsx", ".js")
        ):

            return "code"


        return "config"