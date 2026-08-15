from __future__ import annotations

from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.generators.generator_context import GeneratorContext


def create_generator_context(
    spec,
    step: BuildStep,
    changes=None,
    project_state=None,
):

    return GeneratorContext(
        spec=spec,

        step=step,

        builder=FileBuilder(),

        changes=changes or [],

        project_state=project_state,

        is_update=bool(changes),
    )
