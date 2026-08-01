from core.registry.tool_registry import ToolRegistry


def main():

    registry = ToolRegistry()

    terminal = registry.get("run_terminal")

    result = terminal.execute(
        "python3 workspace/sandbox/output.py"
    )

    print("\nSuccess:", result["success"])
    print("Return Code:", result["return_code"])

    print("\nSTDOUT")
    print(result["stdout"])

    print("\nSTDERR")
    print(result["stderr"])


if __name__ == "__main__":
    main()