import subprocess


class CommandRunner:

    def run(self, command, cwd=None):

        process = subprocess.Popen(
            command,
            cwd=cwd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        return process
