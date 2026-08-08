from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class DashboardState:
    """
    Tracks generated X337 applications.
    """

    project_name: str = ""

    project_path: str = ""

    files: List[str] = field(
        default_factory=list
    )

    components: List[str] = field(
        default_factory=list
    )

    pages: List[str] = field(
        default_factory=list
    )

    services: List[str] = field(
        default_factory=list
    )

    status: str = "idle"


    def scan_project(self):

        root = Path(
            self.project_path
        )


        if not root.exists():

            self.status = "missing"

            return


        self.files = []


        for file in root.rglob("*"):

            if file.is_file():

                self.files.append(
                    str(
                        file.relative_to(root)
                    )
                )


        self.detect_assets()

        self.status = "ready"



    def detect_assets(self):

        self.components = []

        self.pages = []

        self.services = []


        for file in self.files:


            if "components/" in file:

                self.components.append(
                    Path(file).stem
                )


            elif "pages/" in file:

                self.pages.append(
                    Path(file).stem
                )


            elif "services/" in file:

                self.services.append(
                    Path(file).stem
                )



    def summary(self):

        return {

            "project":
                self.project_name,

            "status":
                self.status,

            "files":
                len(self.files),

            "components":
                self.components,

            "pages":
                self.pages,

            "services":
                self.services

        }
