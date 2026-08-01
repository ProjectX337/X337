import os


from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult





class FileManagerAgent(BaseAgent):


    AGENT_NAME = "FileManager"


    DESCRIPTION = (

        "Creates and manages project files."

    )


    CAPABILITIES = [

        "file_management"

    ]


    VERSION = "2.0.0"


    ENABLED = True





    def __init__(
        self,
        app=None
    ):


        super().__init__(

            app=app

        )






    def create_project_directory(
        self,
        name
    ):


        path = os.path.join(

            "workspace",

            "projects",

            name

        )


        os.makedirs(

            path,

            exist_ok=True

        )


        return path







    def write_files(
        self,
        project_path,
        files
    ):


        created = []



        for relative_path, content in files.items():


            file_path = os.path.join(

                project_path,

                relative_path

            )



            directory = os.path.dirname(

                file_path

            )



            os.makedirs(

                directory,

                exist_ok=True

            )



            with open(

                file_path,

                "w"

            ) as file:


                file.write(

                    content

                )



            created.append(

                relative_path

            )



        return created






    def execute(
        self,
        task
    ):


        self.log(

            "Managing project files..."

        )



        project = self.recall(

            "generated_project"

        )



        if not project:


            return TaskResult(

                success=False,

                agent=self.name,

                task=task.title,

                result="No generated project found."

            )





        project_name = project.get(

            "name"

        )



        files = project.get(

            "files",

            {}

        )



        project_path = self.create_project_directory(

            project_name

        )



        created_files = self.write_files(

            project_path,

            files

        )



        task.history.append(

            "FileManager created project structure"

        )



        return TaskResult(

            success=True,

            agent=self.name,

            task=task.title,

            result={

                "project": project_name,

                "path": project_path,

                "files": created_files

            }

        )
