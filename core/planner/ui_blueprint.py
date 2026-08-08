from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class UIPage:

    name: str

    layout: str

    components: List[str] = field(default_factory=list)


    def to_dict(self):

        return {
            "name": self.name,
            "layout": self.layout,
            "components": self.components
        }



@dataclass
class UIBlueprint:

    application: str

    pages: List[UIPage] = field(default_factory=list)

    theme: Dict = field(default_factory=dict)


    def to_dict(self):

        return {
            "application": self.application,
            "pages": [
                page.to_dict()
                for page in self.pages
            ],
            "theme": self.theme
        }
