from agents.director.director import DirectorAgent


def main():
    director = DirectorAgent()

    director.start()

    while True:
        command = input("\nX337 > ").strip()

        if command == "exit":
            print("[System] Goodbye.")
            break

        elif command == "status":
            print("[System] Director Agent is online.")

        elif command == "help":
            print("Available commands:")
            print("- help")
            print("- status")
            print("- task")
            print("- exit")

        elif command == "task":
            task = input("Describe your task: ")
            director.receive_task(task)

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()