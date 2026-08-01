from core.memory.persistent_memory import PersistentMemory



class MemoryManager:


    def __init__(
        self
    ):


        #
        # Persistent long-term storage
        #

        self.persistent = PersistentMemory()



    # ---------------------------------
    # Store memory
    # ---------------------------------

    def remember(
        self,
        key,
        value
    ):


        self.persistent.remember(

            key,

            value

        )


        return value



    # ---------------------------------
    # Retrieve memory
    # ---------------------------------

    def recall(
        self,
        key,
        default=None
    ):


        value = self.persistent.recall(

            key

        )


        if value is None:


            return default



        return value



    # ---------------------------------
    # Compatibility aliases
    # ---------------------------------

    def store(
        self,
        key,
        value
    ):


        """
        Alias for remember().

        Allows agents to use:
        memory.store(key,value)
        """


        return self.remember(

            key,

            value

        )



    def retrieve(
        self,
        key,
        default=None
    ):


        """
        Alias for recall().

        Allows agents to use:
        memory.retrieve(key)
        """


        return self.recall(

            key,

            default

        )



    # ---------------------------------
    # Delete memory
    # ---------------------------------

    def forget(
        self,
        key
    ):


        data = self.persistent.data



        if key in data:


            del data[key]


            self.persistent.save()



        return True



    # ---------------------------------
    # View all memory
    # ---------------------------------

    def all(
        self
    ):


        return self.persistent.data