from __future__ import annotations


def project_exists(
    context,
) -> bool:

    return (
        context is not None
        and context.project is not None
    )


def execution_succeeded(
    result,
) -> bool:

    return result.success
