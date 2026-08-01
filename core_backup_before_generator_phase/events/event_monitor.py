from core.events.event_types import EventTypes



class EventMonitor:


    def __init__(self):

        self.events = []



    def attach(
        self,
        event_bus
    ):


        event_types = [

            EventTypes.TASK_STARTED,

            EventTypes.TASK_ACCEPTED,

            EventTypes.WORKFLOW_CREATED,

            EventTypes.CODE_GENERATED,

            EventTypes.CODE_EXECUTED,

            EventTypes.TEST_STARTED,

            EventTypes.TEST_COMPLETED,

            EventTypes.REVIEW_STARTED,

            EventTypes.REVIEW_APPROVED,

            EventTypes.TASK_COMPLETED,

            EventTypes.TASK_FAILED

        ]



        for event_type in event_types:


            event_bus.subscribe(

                event_type,

                self.handle

            )



    def handle(
        self,
        event
    ):


        self.events.append(
            event
        )


        print(

            f"📡 {event.source:<10} {event.type}"

        )



    def history(self):

        return self.events