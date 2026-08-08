from pathlib import Path


class FileExplorer:
    """
    Explores generated applications.
    """

    def scan(
        self,
        project_path
    ):

        root = Path(project_path)

        files = []


        for file in root.rglob("*"):

            if file.is_file():

                files.append(
                    {
                        "path":
                            str(
                                file.relative_to(root)
                            ),

                        "type":
                            file.suffix
                    }
                )


        return {
            "project":
                root.name,

            "files":
                files,

            "count":
                len(files)
        } 