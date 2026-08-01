from core.brain.brain import X337Brain


class TestTask:

    title = "Create Python calculator"



brain = X337Brain()


result = brain.think(
    TestTask()
)


print(result)
