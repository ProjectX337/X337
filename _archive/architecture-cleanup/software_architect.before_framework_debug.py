from __future__ import annotations

from core.spec.project_spec import ProjectSpec
from core.registry.architecture_registry import ArchitectureRegistry


class SoftwareArchitect:
    """
    X337 Software Architect

    Designs the project using metadata from the
    Architecture Registry instead of hardcoded logic.
    """

    def __init__(self):

        self.registry = ArchitectureRegistry()

    # ---------------------------------------------------------

    def design(
        self,
        spec: ProjectSpec,
    ) -> ProjectSpec:

        architecture = self.registry.get(spec.framework)

        #
        # Language
        #

        spec.language = architecture.language

        #
        # Features
        #

        for feature in architecture.default_features:
            spec.add_feature(feature)

        #
        # Architecture name
        #

        spec.architecture = architecture.name

        #
        # Metadata
        #

        spec.metadata["template"] = architecture.template
        spec.metadata["tester"] = architecture.tester

        return spec