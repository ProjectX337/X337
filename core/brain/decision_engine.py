from core.learning.performance_tracker import PerformanceTracker



class DecisionEngine:


    def __init__(
        self,
        memory=None
    ):


        #
        # Default capability priority
        #

        self.execution_order = [

            "research",

            "writing",

            "coding",

            "testing",

            "review"

        ]



        #
        # Category workflows
        #

        self.category_workflows = {


            "education": [

                "research",

                "writing",

                "coding",

                "testing",

                "review"

            ],



            "software": [

                "coding",

                "testing",

                "review"

            ],



            "data_analysis": [

                "research",

                "coding",

                "review"

            ],



            "research": [

                "research",

                "writing",

                "review"

            ]

        }



        #
        # Agent performance learning
        #

        self.performance = None


        if memory:

            self.performance = PerformanceTracker(

                memory

            )



    def decide(
        self,
        analysis
    ):


        category = analysis.get(

            "category",

            "general"

        )


        capabilities = analysis.get(

            "capabilities",

            []

        )



        #
        # Select workflow template
        #

        priority = self.category_workflows.get(

            category,

            self.execution_order

        )



        workflow = []



        for capability in priority:


            if capability in capabilities:


                workflow.append(

                    capability

                )



        #
        # Show performance influence
        #

        if self.performance:


            leaderboard = self.performance.leaderboard()



            if leaderboard:


                print(

                    "🧠 Adaptive performance data:"

                )


                for agent, score in leaderboard:


                    print(

                        f"{agent}: {round(score * 100)}%"

                    )



        return workflow