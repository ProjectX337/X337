import time

from core.memory.memory_manager import MemoryManager

from core.learning.performance_tracker import PerformanceTracker



class QueueExecutor:


    def __init__(
        self,
        registry,
        queue
    ):


        self.registry = registry

        self.queue = queue


        #
        # Use shared application memory
        #

        if hasattr(registry, "app") and hasattr(
            registry.app,
            "memory"
        ):

            self.memory = registry.app.memory

        else:

            self.memory = MemoryManager()



        #
        # Agent performance tracking
        #

        self.performance = PerformanceTracker(

            self.memory

        )



    def process(
        self,
        task
    ):


        idle_cycles = 0


        max_idle_cycles = 5



        while idle_cycles < max_idle_cycles:


            if self.queue.empty():


                idle_cycles += 1


                time.sleep(0.5)


                continue



            idle_cycles = 0



            item = self.queue.next()



            agent_name = item.get(

                "agent"

            )


            reason = item.get(

                "reason",

                "Unknown"

            )



            print(

                f"⚡ QueueExecutor running: {agent_name}"

            )


            print(

                f"Reason: {reason}"

            )



            agent = self.registry.get(

                agent_name

            )



            if agent is None:


                print(

                    f"⚠️ Agent not found: {agent_name}"

                )


                continue



            try:


                result = agent.execute(

                    task

                )



                print(

                    f"✅ {agent_name} completed"

                )



                #
                # Record successful execution
                #

                self.performance.record(

                    agent_name,

                    True

                )



                if result:


                    task.history.append(

                        f"{agent_name} executed from queue"

                    )



            except Exception as error:


                print(

                    f"❌ {agent_name} failed: {error}"

                )



                #
                # Record failed execution
                #

                self.performance.record(

                    agent_name,

                    False

                )



                task.history.append(

                    f"{agent_name} failed: {error}"

                )



        return True