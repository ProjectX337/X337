import time


class RuntimeEvents:


    def __init__(self):

        self.events = []


    def emit(
        self,
        event,
        session
    ):

        self.events.append(

            {
                "event": event,

                "session":
                    session.id,

                "name":
                    session.name,

                "time":
                    time.time()
            }

        )


    def list(
        self,
        session_id=None
    ):

        if session_id:

            return [
                e
                for e in self.events
                if e["session"] == session_id
            ]

        return self.events
