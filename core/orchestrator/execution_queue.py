class ExecutionQueue:


    def __init__(self):

        self.queue = []



    def add(
        self,
        item
    ):

        self.queue.append(
            item
        )



    def next(
        self
    ):


        if self.queue:

            return self.queue.pop(0)


        return None



    def empty(
        self
    ):

        return len(self.queue) == 0



    def all(
        self
    ):

        return self.queue