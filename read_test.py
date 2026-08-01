from core.registry.tool_registry import ToolRegistry


def main():

    registry = ToolRegistry()

    read_tool = registry.get("read_file")

    contents = read_tool.execute(
        "workspace/sandbox/output.py"
    )

    print("\n===== FILE CONTENTS =====\n")
    print(contents)


if __name__ == "__main__":
    main()