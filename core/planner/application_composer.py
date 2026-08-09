from dataclasses import dataclass, field

from core.planner.feature_planner import FeaturePlanner
from core.templates.template_composer import (
    PageBlueprint,
)


@dataclass
class ApplicationPlan:
    name: str

    pages: list = field(
        default_factory=list
    )

    components: list[str] = field(
        default_factory=list
    )

    services: list[str] = field(
        default_factory=list
    )

    features: list[str] = field(
        default_factory=list
    )


class ApplicationComposer:
    """
    Compatibility adapter for older application composition code.

    The canonical feature representation is FeatureSpec.
    """

    def __init__(self) -> None:
        self.feature_planner = FeaturePlanner()

    def compose(
        self,
        prompt,
    ) -> ApplicationPlan:

        if hasattr(prompt, "original"):
            result = self.feature_planner.plan_application(
                parsed=prompt
            )
        else:
            result = self.feature_planner.plan_application(
                prompt=prompt
            )

        pages = []

        for page in result["pages"]:
            pages.append(
                PageBlueprint(
                    name=page["name"],
                    route=page["route"],
                    components=page["components"],
                )
            )

        feature_names = [
            feature.name
            for feature in result["features"]
        ]

        return ApplicationPlan(
            name="generated_app",
            pages=pages,
            components=result["components"],
            services=result["services"],
            features=feature_names,
        )
