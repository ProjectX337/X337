class ToolResult:

    def __init__(
        self,
        success: bool,
        data=None,
        message: str = "",
    ):
        self.success = success
        self.data = data
        self.message = message

    def __repr__(self):
        return (
            f"ToolResult(success={self.success}, "
            f"message='{self.message}')"
        )