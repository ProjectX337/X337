from pathlib import Path


class FileGenerator:

    def __init__(self):

        self.output_root = Path(
            "core/generator/generated_projects"
        )


    def create_project(self, name, files):

        project_name = self._safe_name(name)

        project_dir = (
            self.output_root /
            project_name
        )

        project_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        created = []

        for file_path, content in files.items():

            target = (
                project_dir /
                file_path
            )

            target.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            target.write_text(
                content,
                encoding="utf-8"
            )

            created.append(file_path)

        return {
            "project": name,
            "directory": str(project_dir),
            "files": created
        }


    def _safe_name(self, name):

        return (
            name.lower()
            .strip()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
        )
