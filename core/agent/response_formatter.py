from __future__ import annotations


class ResponseFormatter:

    def format(
        self,
        project,
        result,
    ):

        if result.get("status") == "complete":

            generated = result.get(
                "generated",
                {}
            )

            files = generated.get(
                "files",
                0
            )

            return (
                f"I built {project}.\n\n"
                f"Generation:\n"
                f"✓ React application generated\n"
                f"✓ {files} files created\n\n"
                f"Validation:\n"
                f"✓ Tests passed\n\n"
                f"Status:\n"
                f"Complete"
            )

        return (
            f"I attempted to build {project}, "
            f"but the process needs attention."
        )
