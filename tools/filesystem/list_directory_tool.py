from pathlib import Path

from tools.base.base_tool import BaseTool


class ListDirectoryTool(BaseTool):

    def __init__(self):
        super().__init__("List Directory")

    def execute(self, path: str):

        self.log(f"Listing: {path}")

        directory = Path(path)

        if not directory.exists():
            raise FileNotFoundError(path)

        items = []

        for item in directory.iterdir():
            items.append(item.name)

        self.log(f"Found {len(items)} item(s).")

        return sorted(items)