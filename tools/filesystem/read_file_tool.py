from pathlib import Path

from tools.base.base_tool import BaseTool


class ReadFileTool(BaseTool):

    def __init__(self):
        super().__init__("Read File")

    def execute(self, path: str):

        self.log(f"Reading file: {path}")

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(path)

        contents = file.read_text()

        self.log("Read successful.")

        return contents