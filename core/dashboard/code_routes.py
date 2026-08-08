import os


IGNORE = {
    "node_modules",
    ".git",
    "dist",
    "__pycache__"
}


def list_files(project_path):

    files = []

    for root, dirs, filenames in os.walk(project_path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE
        ]

        for filename in filenames:

            full = os.path.join(
                root,
                filename
            )

            relative = os.path.relpath(
                full,
                project_path
            )

            files.append(relative)

    return files



def read_file(project_path, path):

    full_path = os.path.join(
        project_path,
        path
    )

    if not os.path.exists(full_path):

        return {
            "error":
            "File not found"
        }


    with open(
        full_path,
        "r"
    ) as f:

        return {
            "file": path,
            "code": f.read()
        }
