from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BuildStep:
    """
    A single generation task.
    """

    # Human-readable name
    name: str

    # Generator responsible for this step
    generator: str

    # Short description
    description: str

    # Output directory relative to the project root
    output_directory: str

    # Execution priority (lower runs first)
    priority: int = 100

    # Names of BuildSteps that must complete first
    depends_on: list[str] = field(
        default_factory=list
    )

    # Whether this step is optional
    optional: bool = False


@dataclass(slots=True)
class BuildPlan:
    """
    Ordered generation plan produced from a ProjectSpec.
    """

    steps: list[BuildStep] = field(
        default_factory=list
    )

    def add(
        self,
        *,
        name: str,
        generator: str,
        description: str,
        output_directory: str,
        priority: int = 100,
        depends_on: list[str] | None = None,
        optional: bool = False,
    ) -> None:

        self.steps.append(

            BuildStep(

                name=name,

                generator=generator,

                description=description,

                output_directory=output_directory,

                priority=priority,

                depends_on=depends_on or [],

                optional=optional,

            )

        )

    def ordered_steps(self) -> list[BuildStep]:

        return sorted(
            self.steps,
            key=lambda step: step.priority,
        )
