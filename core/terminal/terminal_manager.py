from core.terminal.command_runner import CommandRunner


class TerminalManager:

    def __init__(self):
        self.runner = CommandRunner()


    def start(self, command, cwd=None):

        return self.runner.run(
            command,
            cwd
        )
