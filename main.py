from core.application.application_context import ApplicationContext

from core.registry.agent_registry import AgentRegistry

from core.models.task import Task

from core.orchestrator.orchestrator import Orchestrator



def main():


    print()

    print("# 🚀 X337 Multi-Agent System")

    print()



    task_input = input(
        "Enter a task: "
    )



    #
    # Create shared application context
    #

    app = ApplicationContext()



    #
    # Load agents using shared context
    #

    registry = AgentRegistry(
        app
    )



    #
    # Create orchestrator
    #

    orchestrator = Orchestrator(

        registry,

        app.event_bus,

        app.execution_queue

    )



    #
    # Create task
    #

    task = Task(
        task_input
    )



    #
    # Execute workflow
    #

    result = orchestrator.execute(
        task
    )



    print()

    print("=" * 50)

    print("✅ WORKFLOW COMPLETE")

    print("=" * 50)

    print()



    if hasattr(result, "agent"):

        print(
            "Agent:",
            result.agent
        )


        print()


        print(
            "Success:",
            result.success
        )


    else:


        print(
            "Agent: Orchestrator"
        )


        print()


        print(
            "Success: True"
        )



    print()

    print(
        "Task History:"
    )



    for event in task.history:


        print(
            "•",
            event
        )




if __name__ == "__main__":

    main()