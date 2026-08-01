class PlanningPipelineError(Exception):
    """
    Raised when a planning stage cannot execute because
    one or more required context fields are missing.
    """
    pass
