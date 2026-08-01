from core.brain.task_analyzer import TaskAnalyzer
from core.brain.decision_engine import DecisionEngine

from core.learning.workflow_history import WorkflowHistory
from core.learning.performance_tracker import PerformanceTracker
from core.learning.agent_ranker import AgentRanker

from core.memory.memory_manager import MemoryManager


class X337Brain:


    def __init__(
        self
    ):


        #
        # Reasoning systems
        #

        self.analyzer = TaskAnalyzer()

        self.decision_engine = DecisionEngine()



        #
        # Shared memory
        #

        self.memory = MemoryManager()



        #
        # Learning systems
        #

        self.learning = WorkflowHistory(
            self.memory
        )


        self.performance = PerformanceTracker(
            self.memory
        )


        #
        # Agent intelligence
        #

        self.agent_ranker = AgentRanker(
            self.performance
        )





    # ---------------------------------
    # Think
    # ---------------------------------

    def think(
        self,
        task
    ):


        #
        # Analyze task
        #

        analysis = self.analyzer.analyze(
            task
        )


        category = analysis.get(
            "category",
            "general"
        )



        print(
            "🧠 Task analysis:"
        )


        print(
            analysis
        )



        #
        # Check learned workflows
        #

        learned = self.learning.best_workflow(
            category
        )



        if learned:


            print(
                "🧠 Learned workflow selected:"
            )


            print(
                learned
            )


            return learned





        #
        # Generate new workflow
        #

        workflow = self.decision_engine.decide(
            analysis
        )


        print(
            "🧠 New workflow generated:"
        )


        print(
            workflow
        )


        return workflow





    # ---------------------------------
    # Agent Intelligence
    # ---------------------------------

    def rank_agents(
        self
    ):


        rankings = (
            self.agent_ranker.rank_agents()
        )


        print(
            "🧠 Agent rankings:"
        )


        print(
            rankings
        )


        return rankings





    # ---------------------------------
    # Recommend Agent
    # ---------------------------------

    def recommend_agent(
        self,
        capability
    ):


        agent = (
            self.agent_ranker.recommend(
                capability
            )
        )


        if agent:


            print(
                f"🧠 Recommended agent for {capability}: {agent}"
            )


        return agent





    # ---------------------------------
    # Learn Workflow
    # ---------------------------------

    def learn(
        self,
        task,
        workflow,
        success=True,
        score=100
    ):


        self.learning.record(

            task,

            workflow,

            success,

            score

        )


        print(
            "🧠 Workflow learned and stored."
        )
