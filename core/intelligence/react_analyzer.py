from __future__ import annotations

from pathlib import Path


class ReactAnalyzer:
    """
    Understands React application structure.

    Converts source files into architectural signals.
    """

    def analyze(
        self,
        snapshot,
    ):

        result = {
            "pages": [],
            "components": [],
            "features": [],
            "routes": [],
            "hooks": [],
        }

        for file in snapshot.files:

            path = Path(file)

            parts = path.parts


            if "pages" in parts:

                result["pages"].append(
                    path.stem
                )


            if "components" in parts:

                result["components"].append(
                    path.stem
                )


            if "features" in parts:

                index = parts.index(
                    "features"
                )

                if len(parts) > index + 1:
                    result["features"].append(
                        parts[index + 1]
                    )


            if path.suffix in (
                ".ts",
                ".tsx",
            ):

                if path.stem.startswith(
                    "use"
                ):
                    result["hooks"].append(
                        path.stem
                    )


        result["pages"] = sorted(
            set(result["pages"])
        )

        result["components"] = sorted(
            set(result["components"])
        )

        result["features"] = sorted(
            set(result["features"])
        )

        result["hooks"] = sorted(
            set(result["hooks"])
        )

        return result
