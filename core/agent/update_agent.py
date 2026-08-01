from __future__ import annotations

from core.agent.project_state import ProjectState
from core.agent.change_engine import ChangeEngine
from core.spec.models.feature_spec import FeatureSpec


class UpdateAgent:
    """
    Applies changes to an existing project.
    """

    def __init__(self):

        self.state = ProjectState()

        self.engine = ChangeEngine()


    def apply(
        self,
        message: str,
        context=None,
    ):

        project = None

        if context:

            if isinstance(context, dict):

                project = context.get(
                    "project"
                )

            else:

                project = getattr(
                    context,
                    "spec",
                    None,
                )


        if project:

            self.state.update(
                project
            )


        changes = self.engine.detect(
            message
        )


        for feature in changes["features"]:

            self.state.record_change(
                feature
            )


            if self.state.project:

                from core.spec.models.feature_spec import FeatureSpec

                exists = any(
                    f.name == feature
                    for f in self.state.project.feature_models
                )

                if not exists:

                    self.state.project.feature_models.append(
                        FeatureSpec(
                            name=feature,
                            slug=(
                                feature
                                .lower()
                                .replace(" ", "_")
                                .replace("-", "_")
                            ),
                            description=f"{feature} feature",
                        )
                    )


        return self.state
