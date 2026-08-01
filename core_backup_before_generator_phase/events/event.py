class Event:


    def __init__(
        self,
        event_type,
        source,
        data=None
    ):


        self.type = event_type


        self.source = source


        self.data = data or {}



    def __repr__(self):


        return (
            f"Event("
            f"type={self.type}, "
            f"source={self.source}"
            f")"
        )