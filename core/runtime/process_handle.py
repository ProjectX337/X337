from dataclasses import dataclass

from core.runtime.runtime_process import RuntimeProcess


@dataclass
class ProcessHandle:

    runtime_process: RuntimeProcess

    popen_process: object

    def pid(self):
        return self.runtime_process.pid
