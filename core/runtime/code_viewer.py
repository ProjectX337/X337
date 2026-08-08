from pathlib import Path


class CodeViewer:
    """
    Reads generated application source files.
    Used by X337 UI to display generated code.
    """


    def __init__(
        self,
        root="workspace/generated"
    ):

        self.root = Path(root)



    def get_file(
        self,
        project_name,
        file_path
    ):

        path = (
            self.root /
            project_name /
            file_path
        )


        if not path.exists():

            return {

                "status":
                    "error",

                "message":
                    "File not found"

            }



        return {

            "status":
                "success",

            "file":
                file_path,

            "language":
                self.detect_language(
                    path
                ),

            "content":
                path.read_text()

        }



    def detect_language(
        self,
        path
    ):

        extension = (
            path.suffix
        )


        languages = {

            ".tsx":
                "typescript-react",

            ".ts":
                "typescript",

            ".jsx":
                "javascript-react",

            ".js":
                "javascript",

            ".json":
                "json",

            ".css":
                "css",

            ".html":
                "html"

        }


        return languages.get(
            extension,
            "text"
        )