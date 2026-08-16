from __future__ import annotations


from core.intelligence.react_analyzer import (
    ReactAnalyzer,
)


class ApplicationUnderstanding:
    """
    Produces semantic understanding
    of an existing application.
    """


    def __init__(
        self,
        analyzers=None,
    ):

        self.react = ReactAnalyzer()


    def understand(
        self,
        snapshot,
    ):

        return {
            "project": snapshot.project_name,

            "framework": snapshot.framework,

            "language": snapshot.language,

            "react": self.react.analyze(
                snapshot
            ),

            "files": len(
                snapshot.files
            ),
        }
