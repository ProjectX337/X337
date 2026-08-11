from core.events.event_types import EventTypes

from core.orchestrator.execution_queue import ExecutionQueue

from core.orchestrator.queue_executor import QueueExecutor

from core.orchestrator.task_router import TaskRouter

from core.learning.workflow_history import WorkflowHistory

from core.memory.memory_manager import MemoryManager




class Orchestrator:


    def __init__(
        self,
        registry,
        event_bus=None,
        execution_queue=None,
        memory=None
    ):


        self.registry = registry


        self.event_bus = event_bus



        self.execution_queue = (

            execution_queue

            if execution_queue

            else ExecutionQueue()

        )



        self.router = TaskRouter(

            self.execution_queue

        )



        self.queue_executor = QueueExecutor(

            self.registry,

            self.execution_queue

        )



        #
        # Shared memory
        #

        self.memory = (

            memory

            if memory

            else MemoryManager()

        )



        #
        # Learning system
        #

        self.learning = WorkflowHistory(

            self.memory

        )




        if self.event_bus:

            self.register_event_handlers()






    # ---------------------------------
    # Event Registration
    # ---------------------------------

    def register_event_handlers(
        self
    ):


        self.event_bus.subscribe(

            EventTypes.WORKFLOW_CREATED,

            self.queue_workflow

        )







    # ---------------------------------
    # Workflow Queue Builder
    # ---------------------------------

    def queue_workflow(
        self,
        event,
    ):

        workflow = event.data.get(
            "workflow",
            [],
        )

        print(
            "⚡ Workflow received. "
            "Adding agents to queue."
        )

        seen = set()

        for agent_name in workflow:

            if agent_name in seen:
                continue

            seen.add(agent_name)

            print(
                f"➕ Queue <- {agent_name}"
            )

            self.execution_queue.add(
                {
                    "agent": agent_name,
                    "reason": "WorkflowCreated",
                }
            )


    # ---------------------------------
    # Execute Workflow
    # ---------------------------------

    def execute(
        self,
        task
    ):


        task.history.append(

            "Queue execution started"

        )



        success = True



        try:


            #
            # Send task to Planner
            #

            self.router.route(

                task

            )



            #
            # Execute workflow
            #

            self.queue_executor.process(

                task

            )



        except Exception as error:


            success = False


            task.history.append(

                f"Orchestrator failed: {error}"

            )



            print(

                f"❌ Orchestrator failed: {error}"

            )





        #
        # Save workflow learning
        #

        try:


            self.learning.record(

                task,

                success

            )


            print(

                "🧠 Workflow learned and stored."

            )



        except Exception as error:


            print(

                f"⚠ Learning save failed: {error}"

            )







        task.history.append(

            "Queue execution completed"

        )



        return task
