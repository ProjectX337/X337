from tools.filesystem.write_file_tool import WriteFileTool
from tools.filesystem.read_file_tool import ReadFileTool
from tools.filesystem.list_directory_tool import ListDirectoryTool
from tools.terminal.run_terminal_tool import RunTerminalTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "write_file": WriteFileTool(),
            "read_file": ReadFileTool(),
            "list_directory": ListDirectoryTool(),
            "run_terminal": RunTerminalTool(),
        }

    def get(self, tool_name):

        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        return self.tools[tool_name]

    def list_tools(self):
        return list(self.tools.keys())