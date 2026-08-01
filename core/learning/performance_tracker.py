import time




class PerformanceTracker:


    def __init__(
        self,
        memory=None
    ):

        self.memory = memory

        self.records = {}





    #
    # Compatibility method
    #
    # Existing X337 calls this
    #

    def record(
        self,
        agent,
        success=True,
        execution_time=0
    ):


        self.records[agent] = {


            "success": success,


            "execution_time": execution_time,


            "score": self.calculate_score(

                success,

                execution_time

            )

        }





    def start_agent(
        self,
        agent
    ):

        self.records[agent] = {

            "start": time.time()

        }





    def finish_agent(
        self,
        agent,
        success=True
    ):


        if agent not in self.records:

            self.start_agent(agent)



        elapsed = (

            time.time()

            -

            self.records[agent].get(

                "start",

                time.time()

            )

        )



        self.record(

            agent,

            success,

            elapsed

        )






    def calculate_score(
        self,
        success,
        execution_time
    ):


        score = 100



        if not success:

            score -= 50



        score -= min(

            execution_time,

            20

        )



        return round(

            max(score,0),

            2

        )






    def score_agent(
        self,
        agent
    ):


        return self.records.get(

            agent,

            {}

        ).get(

            "score",

            0

        )






    def get_rankings(
        self
    ):


        rankings = {}



        for agent in self.records:


            rankings[agent] = self.score_agent(

                agent

            )



        return rankings
