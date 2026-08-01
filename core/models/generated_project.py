class GeneratedProject:


    def __init__(
        self,
        name,
        project_type,
        description="",
        files=None
    ):

        self.name = name

        self.project_type = project_type

        self.description = description

        self.files = files or {}



    def add_file(
        self,
        path,
        content
    ):

        self.files[path] = content



    def file_count(
        self
    ):

        return len(self.files)



    def to_dict(
        self
    ):

        return {

            "name": self.name,

            "project_type": self.project_type,

            "description": self.description,

            "files": self.files,

            "file_count": self.file_count()

        }
