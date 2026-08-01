from pathlib import Path

from tools.base.base_tool import BaseTool


class WriteFileTool(BaseTool):

    def __init__(self):
        super().__init__("Write File")

    def execute(self, path: str, content: str):

        self.log(f"Writing file: {path}")

        file = Path(path)

        file.parent.mkdir(parents=True, exist_ok=True)

        file.write_text(content)

        self.log("File written successfully.")

        return True