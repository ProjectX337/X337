import time

from core.memory.memory_manager import MemoryManager

from core.learning.performance_tracker import PerformanceTracker

from core.events.event_types import EventTypes



class QueueExecutor:


    MAX_REPAIRS = 3



    def __init__(
        self,
        registry,
        queue
    ):


        self.registry = registry

        self.queue = queue


        if hasattr(registry, "app") and hasattr(
            registry.app,
            "memory"
        ):

            self.memory = registry.app.memory

        else:

            self.memory = MemoryManager()



        self.performance = PerformanceTracker(

            self.memory

        )


        self.repair_attempts = 0




    def add_repair_workflow(
        self
    ):


        if self.repair_attempts >= self.MAX_REPAIRS:


            print(
                "⚠ Maximum repair attempts reached."
            )


            return



        self.repair_attempts += 1



        print(
            f"🔧 Starting repair cycle {self.repair_attempts}"
        )



        self.queue.add(

            {

                "agent": "Coder",

                "reason": "RepairRequired"

            }

        )



        self.queue.add(

            {

                "agent": "FileManager",

                "reason": "RepairRequired"

            }

        )



        self.queue.add(

            {

                "agent": "Tester",

                "reason": "RepairValidation"

            }

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



                success = True



                if result and hasattr(
                    result,
                    "success"
                ):

                    success = result.success




                self.performance.record(

                    agent_name,

                    success

                )





                #
                # Tester failed
                #
                # Start repair loop
                #

                if (

                    agent_name == "Tester"

                    and

                    not success

                ):


                    print(

                        "🚨 Tester failure detected."

                    )


                    self.memory.store(

                        "repair_required",

                        {

                            "task": task.title,

                            "reason": result.result

                            if result

                            else "Unknown failure"

                        }

                    )


                    self.add_repair_workflow()



                if result:


                    task.history.append(

                        f"{agent_name} executed from queue"

                    )





            except Exception as error:


                print(

                    f"❌ {agent_name} failed: {error}"

                )



                self.performance.record(

                    agent_name,

                    False

                )



                task.history.append(

                    f"{agent_name} failed: {error}"

                )



        return True
