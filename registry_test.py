from core.registry.tool_registry import ToolRegistry


def main():

    registry = ToolRegistry()

    print("Available tools:")

    for tool in registry.list_tools():
        print("-", tool)


if __name__ == "__main__":
    main()