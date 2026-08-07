from core.spec.project_spec import ProjectSpec


class ExecutionPlanner:
    """
    Converts a ProjectSpec into an execution workflow.
    """

    def plan(self, spec: ProjectSpec) -> list[str]:
        workflow = []

        if getattr(spec, "feature_models", None):
            workflow.append("Coder")

        workflow.extend(
            [
                "FileManager",
                "Tester",
                "Reviewer",
            ]
        )

        return workflow