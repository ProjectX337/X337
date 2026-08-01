class EventBus:


    def __init__(self):

        self.listeners = {}



    def subscribe(
        self,
        event_type,
        callback
    ):


        if event_type not in self.listeners:

            self.listeners[event_type] = []


        self.listeners[event_type].append(
            callback
        )



    def publish(
        self,
        event
    ):


        listeners = self.listeners.get(
            event.type,
            []
        )


        for callback in listeners:

            callback(event)