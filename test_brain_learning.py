from core.brain.brain import X337Brain


class TestTask:

    def __init__(self, title):

        self.title = title



brain = X337Brain()



tasks = [

    "Create Python calculator",

    "Create AI tutor",

    "Build a REST API",

    "Analyze customer data"

]



for task_name in tasks:


    print("\nTASK:")

    print(task_name)



    result = brain.think(

        TestTask(task_name)

    )


    print("PLAN:")

    print(result)