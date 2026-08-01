class MemoryStore:


    def __init__(self):

        self.data = {}



    def store(
        self,
        key,
        value
    ):

        self.data[key] = value



    def retrieve(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )



    def exists(
        self,
        key
    ):

        return key in self.data



    def all(
        self
    ):

        return self.data