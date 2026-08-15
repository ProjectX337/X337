import time


class RuntimeEvents:


    def __init__(self):

        self.events = []


    def emit(
        self,
        event,
        runtime
    ):

        self.events.append(

            {
                "event": event,

                "runtime":
                    runtime.id,

                "name":
                    runtime.name,

                "time":
                    time.time()
            }

        )


    def list(
        self,
        runtime_id=None
    ):

        if runtime_id:

            return [
                e
                for e in self.events
                if e["runtime"] == runtime_id
            ]

        return self.events
