from core.registry.agent_registry import AgentRegistry


class Orchestrator:

    def __init__(self):

        self.registry = AgentRegistry()

    def execute(self, task):

        final_result = None

        # -------------------------
        # Step 1: Director
        # -------------------------

        director = self.registry.get(
            "Director"
        )

        director.start()

        director.execute(task)

        director.stop()


        # -------------------------
        # Step 2: Planner
        # -------------------------

        planner = self.registry.get(
            "Planner"
        )

        planner.start()

        planner_result = planner.execute(task)

        planner.stop()


        if not planner_result.success:

            return planner_result


        # -------------------------
        # Step 3: Workflow Execution
        # -------------------------

        workflow = task.context.get(
            "workflow"
        )


        if workflow is None:

            raise RuntimeError(
                "Planner did not create workflow."
            )


        task.history.append(
            "Workflow execution started"
        )


        for step in workflow.steps:


            step.status = "Running"


            self.registry.find_by_capability(
                step.capability
            )


            agent = self.registry.best_agent(
                step.capability
            )


            step.assigned_agent = (
                agent.name
            )


            agent.start()


            result = agent.execute(
                task
            )


            agent.stop()


            step.result = result


            if result.success:

                step.status = "Completed"

            else:

                step.status = "Failed"

                return result


            final_result = result


        task.history.append(
            "Workflow execution completed"
        )


        return final_result