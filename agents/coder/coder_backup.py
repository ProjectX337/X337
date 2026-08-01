import re

from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult

from core.events.event import Event

from core.events.event_types import EventTypes

from core.projects.project_generator import ProjectGenerator

from core.coding.code_planner import CodePlanner



class CoderAgent(BaseAgent):


    AGENT_NAME = "Coder"


    DESCRIPTION = (
        "Plans and generates complete software projects."
    )


    CAPABILITIES = [

        "coding"

    ]


    VERSION = "3.0.0"


    ENABLED = True



    def __init__(
        self,
        app=None
    ):

        super().__init__(
            app=app
        )


        self.generator = ProjectGenerator()


        self.code_planner = CodePlanner()





    # ---------------------------------
    # Execute Coding Workflow
    # ---------------------------------

    def execute(
        self,
        task
    ):


        self.log(
            "Planning software architecture..."
        )



        #
        # Step 1:
        # Create code plan
        #

        plan = self.code_planner.analyze(
            task
        )



        self.log(
            f"Code plan created: {plan}"
        )



        #
        # Step 2:
        # Generate project
        #

        self.log(
            "Generating project..."
        )



        project_name = self.create_project_name(

            task.title

        )



        project = self.generator.generate(

            project_name,

            task,

            plan

        )



        #
        # Store project memory
        #

        self.remember(

            "generated_project",

            project

        )


        self.remember(

            "code_plan",

            plan

        )



        task.history.append(

            f"Coder created project {project_name}"

        )



        #
        # Publish event
        #

        self.bus.publish(

            Event(

                EventTypes.CODE_GENERATED,

                self.name,

                {

                    "project": project,

                    "plan": plan

                }

            )

        )



        self.log(

            f"Generated {len(project['files'])} files."

        )



        return TaskResult(

            success=True,

            agent=self.name,

            task=task.title,

            result={

                "project": project,

                "plan": plan

            }

        )





    # ---------------------------------
    # Project Naming
    # ---------------------------------

    def create_project_name(
        self,
        title
    ):


        name = re.sub(

            r'[^a-zA-Z0-9 ]',

            '',

            title

        )


        return "_".join(

            name.lower().split()

        )
