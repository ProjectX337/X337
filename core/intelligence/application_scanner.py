from pathlib import Path

from core.intelligence.application_snapshot import (
    ApplicationSnapshot,
)


class ApplicationScanner:
    """
    Inspects generated applications
    and creates an ApplicationSnapshot.
    """

    def scan(
        self,
        root_path: str,
    ) -> ApplicationSnapshot:

        root = Path(root_path)

        snapshot = ApplicationSnapshot(
            project_name=root.name,
            root_path=str(root),
        )

        for path in root.rglob("*"):

            if path.is_file():

                relative = str(
                    path.relative_to(root)
                )

                snapshot.files.append(
                    relative
                )

            elif path.is_dir():

                relative = str(
                    path.relative_to(root)
                )

                snapshot.directories.append(
                    relative
                )

        self._detect_framework(
            snapshot
        )

        self._detect_language(
            snapshot
        )

        return snapshot


    def _detect_framework(
        self,
        snapshot,
    ):

        files = snapshot.files

        if "package.json" in files:
            snapshot.framework = "javascript"


    def _detect_language(
        self,
        snapshot,
    ):

        if any(
            file.endswith(".tsx")
            for file in snapshot.files
        ):
            snapshot.language = "typescript"

        elif any(
            file.endswith(".jsx")
            for file in snapshot.files
        ):
            snapshot.language = "javascript"
