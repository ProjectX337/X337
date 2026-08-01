from agents.coder.coder import CoderAgent
from agents.writer.writer import WriterAgent
from agents.researcher.researcher import ResearcherAgent
from agents.tester.tester import TesterAgent
from agents.reviewer.reviewer import ReviewerAgent
from agents.planner.planner import PlannerAgent
from agents.director.director import DirectorAgent
from agents.file_manager.file_manager import FileManagerAgent



class AgentRegistry:


    def __init__(
        self,
        app
    ):


        self.app = app


        self.agents = {}


        self.capability_index = {}


        self.load_agents()



    # ---------------------------------
    # Load agents
    # ---------------------------------

    def load_agents(
        self
    ):


        agents = [

            CoderAgent(
                app=self.app
            ),

            DirectorAgent(
                app=self.app
            ),

            PlannerAgent(
                app=self.app
            ),

            ResearcherAgent(
                app=self.app
            ),

            TesterAgent(
                app=self.app
            ),

            ReviewerAgent(
                app=self.app
            ),

            WriterAgent(
                app=self.app
            ),

            FileManagerAgent(
                app=self.app
            )

        ]



        for agent in agents:


            self.agents[agent.name] = agent



            print(

                f"Loaded agent: {agent.name}"

            )



            #
            # Register capabilities
            #

            capabilities = getattr(

                agent,

                "capabilities",

                []

            )



            for capability in capabilities:


                self.capability_index[capability] = agent.name



    # ---------------------------------
    # Get agent
    # ---------------------------------

    def get(
        self,
        name
    ):


        return self.agents.get(

            name

        )



    # ---------------------------------
    # Find agent by capability
    # ---------------------------------

    def find_by_capability(
        self,
        capability
    ):


        agent_name = self.capability_index.get(

            capability

        )


        if not agent_name:

            return None



        return self.agents.get(

            agent_name

        )



    # ---------------------------------
    # Capability map
    # ---------------------------------

    def capabilities(
        self
    ):


        return self.capability_index