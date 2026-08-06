from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult

from core.events.event import Event

from core.events.event_types import EventTypes
from core.planner.project_planner import ProjectPlanner





class PlannerAgent(BaseAgent):


    AGENT_NAME = "Planner"


    DESCRIPTION = (
        "Creates intelligent execution workflows."
    )


    CAPABILITIES = [

        "planning"

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


        self.project_planner = ProjectPlanner()





    # ---------------------------------
    # Analyze Task
    # ---------------------------------

    def analyze_task(
        self,
        task
    ):


        title = task.title.lower()



        capabilities = []



        #
        # Software projects
        #

        if (

            "api" in title

            or

            "software" in title

            or

            "app" in title

            or

            "website" in title

            or

            "application" in title

        ):


            capabilities.extend(

                [

                    "coding",

                    "file_management",

                    "testing",

                    "review"

                ]

            )





        #
        # Education projects
        #

        if (

            "tutor" in title

            or

            "education" in title

            or

            "course" in title

        ):


            capabilities = [

                "research",

                "writing",

                "coding",

                "file_management",

                "testing",

                "review"

            ]





        #
        # Writing tasks
        #

        if (

            "write" in title

            or

            "document" in title

        ):


            capabilities = [

                "research",

                "writing",

                "review"

            ]






        return {


            "category": self.detect_category(task),


            "capabilities": capabilities


        }








    # ---------------------------------
    # Category Detection
    # ---------------------------------

    def detect_category(
        self,
        task
    ):


        title = task.title.lower()



        if "api" in title:

            return "software"



        if "website" in title:

            return "software"



        if "tutor" in title:

            return "education"



        if "write" in title:

            return "writing"



        return "general"







    # ---------------------------------
    # Learned Workflow
    # ---------------------------------

    def get_learned_workflow(
        self
    ):


        try:


            workflow = (

                self.app.learning
                .best_recent_workflow()

            )



            if workflow:


                print(

                    "🧠 Learned workflow selected:"

                )


                print(

                    workflow

                )


                return workflow



        except Exception:


            pass




        return None







    # ---------------------------------
    # Execute Planning
    # ---------------------------------

    def execute(
        self,
        task
    ):


        self.log(

            "Creating execution workflow..."

        )



        analysis = self.analyze_task(

            task

        )


        # ---------------------------------
        # Create canonical ProjectSpec
        # Planner -> Coder contract
        # ---------------------------------

        if "coding" in analysis["capabilities"]:

            print(
                "🧠 Creating ProjectSpec..."
            )

            task.project_spec = self.project_planner.plan(
                task.title
            )




        print(

            "🧠 Task analysis:"

        )


        print(

            analysis

        )



        workflow = self.get_learned_workflow()





        if workflow:


            print(

                "🧠 Brain using learned workflow."

            )



        else:


            workflow = analysis[

                "capabilities"

            ]



            print(

                "🧠 New workflow generated:"

            )


            print(

                workflow

            )






        print(

            "[Planner] Brain plan:",

            workflow

        )






        self.bus.publish(

            Event(

                EventTypes.WORKFLOW_CREATED,

                self.name,

                {

                    "workflow": workflow

                }

            )

        )





        task.history.append(

            "Planner created intelligent workflow"

        )






        return TaskResult(

            success=True,

            agent=self.name,

            task=task.title,

            result={

                "workflow": workflow,

                "analysis": analysis

            }

        )
