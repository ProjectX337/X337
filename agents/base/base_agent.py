from abc import ABC, abstractmethod

from datetime import datetime

from core.models.task import Task

from core.models.task_result import TaskResult



class BaseAgent(ABC):

    """
    Base class for every X337 agent.

    Provides:

        - logging
        - application context
        - event bus
        - shared memory
        - lifecycle management
        - metadata
    """



    AGENT_NAME = "BaseAgent"


    DESCRIPTION = (
        "Base class for all X337 agents."
    )


    CAPABILITIES = []


    VERSION = "1.0.0"


    ENABLED = True




    def __init__(
        self,
        name: str | None = None,
        app=None
    ):


        self.name = (
            name or self.AGENT_NAME
        )


        self.status = "Offline"


        self.created_at = datetime.now()



        #
        # Application Context
        #
        # Uses shared context when provided
        #

        if app:

            self.app = app

        else:

            from core.application.application_context import ApplicationContext

            self.app = ApplicationContext()



        #
        # Event Bus
        #

        self.bus = self.app.bus



        #
        # Logger
        #

        self.logger = self.app.logger



        #
        # Shared Agent Memory
        #
        # All agents can read/write here
        #

        self.memory = self.app.memory




    def start(self):

        self.status = "Online"

        self.log(
            "Started."
        )




    def stop(self):

        self.status = "Offline"

        self.log(
            "Stopped."
        )




    def log(
        self,
        message: str
    ):


        formatted = (
            f"[{self.name}] {message}"
        )


        print(
            formatted
        )


        self.logger.write(
            formatted
        )




    def remember(
        self,
        key,
        value
    ):

        """
        Store information in shared memory.
        """

        self.memory.remember(
            key,
            value
        )




    def recall(
        self,
        key
    ):

        """
        Retrieve information from shared memory.
        """

        return self.memory.recall(
            key
        )




    @classmethod
    def metadata(cls):

        return {

            "name": cls.AGENT_NAME,

            "description": cls.DESCRIPTION,

            "capabilities": cls.CAPABILITIES,

            "version": cls.VERSION,

            "enabled": cls.ENABLED,

        }




    @abstractmethod
    def execute(
        self,
        task: Task
    ) -> TaskResult:

        pass