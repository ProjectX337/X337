from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BuildStep:
    """
    A single generation task.
    """

    name: str
    generator: str
    description: str
    output_directory: str

    priority: int = 100

    depends_on: list[str] = field(
        default_factory=list
    )

    optional: bool = False


@dataclass(slots=True)
class BuildPlan:
    """
    Ordered generation plan produced from a ProjectSpec.

    Build ordering is dependency-aware and deterministic.
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
        """
        Return steps in dependency-safe deterministic order.

        Dependencies always execute before dependents.
        Priority breaks ties between otherwise-independent steps.
        """

        if not self.steps:
            return []

        by_name = {
            step.name: step
            for step in self.steps
        }

        missing: set[str] = set()

        for step in self.steps:
            for dependency in step.depends_on:
                if dependency not in by_name:
                    missing.add(dependency)

        if missing:
            raise ValueError(
                "Build plan contains missing dependencies: "
                + ", ".join(sorted(missing))
            )

        ordered: list[BuildStep] = []
        remaining = set(by_name)

        while remaining:
            ready = [
                by_name[name]
                for name in remaining
                if all(
                    dependency not in remaining
                    for dependency in by_name[name].depends_on
                )
            ]

            if not ready:
                cycle = sorted(remaining)
                raise ValueError(
                    "Build plan contains a dependency cycle involving: "
                    + ", ".join(cycle)
                )

            ready.sort(
                key=lambda step: (
                    step.priority,
                    step.name,
                )
            )

            for step in ready:
                ordered.append(step)
                remaining.remove(step.name)

        return ordered
