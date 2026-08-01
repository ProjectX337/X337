from core.events.event_bus import EventBus

from core.events.event_monitor import EventMonitor

from core.logging.logger import Logger

from core.orchestrator.execution_queue import ExecutionQueue

from core.memory.memory_manager import MemoryManager

from core.brain.brain import X337Brain



class ApplicationContext:


    def __init__(
        self
    ):


        #
        # Event system
        #

        self.event_bus = EventBus()



        #
        # Compatibility layer
        # BaseAgent expects self.bus
        #

        self.bus = self.event_bus



        #
        # Logging
        #

        self.logger = Logger()



        #
        # Shared memory
        #

        self.memory = MemoryManager()



        #
        # Event monitoring
        #

        self.event_monitor = EventMonitor()


        self.event_monitor.attach(

            self.event_bus

        )



        #
        # Execution Queue
        #

        self.execution_queue = ExecutionQueue()



        #
        # Service container
        #

        self.services = {}



        #
        # X337 Brain
        #
        # Central reasoning + learning engine
        #

        self.brain = X337Brain()



        self.register(

            "brain",

            self.brain

        )



        #
        # Register shared services
        #

        self.register(

            "memory",

            self.memory

        )


        self.register(

            "event_bus",

            self.event_bus

        )


        self.register(

            "execution_queue",

            self.execution_queue

        )



    # ---------------------------------
    # Service registration
    # ---------------------------------

    def register(
        self,
        name,
        service
    ):


        self.services[name] = service



    # ---------------------------------
    # Service retrieval
    # ---------------------------------

    def get(
        self,
        name
    ):


        return self.services.get(

            name

        )