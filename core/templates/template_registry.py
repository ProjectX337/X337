import json

from pathlib import Path

from core.templates.template_schema import (
    TemplateDefinition
)


class TemplateRegistry:


    def __init__(
        self,
        path="core/templates/definitions"
    ):

        self.path = Path(path)

        self.templates = {}

        self.load()



    def load(self):

        if not self.path.exists():
            return


        for file in self.path.glob(
            "*.json"
        ):

            data = json.loads(
                file.read_text()
            )

            template = TemplateDefinition(
                **data
            )

            self.templates[
                template.name
            ] = template



    def get(
        self,
        name
    ):

        return self.templates.get(
            name
        )



    def list(
        self
    ):

        return list(
            self.templates.values()
        )