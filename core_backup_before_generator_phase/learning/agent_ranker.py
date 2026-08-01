from core.learning.performance_tracker import PerformanceTracker


class AgentRanker:

    def __init__(
        self,
        performance=None
    ):

        self.performance = (
            performance
            if performance
            else PerformanceTracker()
        )


    #
    # Rank all agents
    #

    def rank_agents(
        self
    ):

        rankings = (
            self.performance.get_rankings()
        )


        return dict(
            sorted(
                rankings.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )


    #
    # Return strongest agent
    #

    def best_agent(
        self
    ):

        rankings = self.rank_agents()


        if not rankings:

            return None


        return next(
            iter(rankings)
        )


    #
    # Agent recommendation
    #

    def recommend(
        self,
        capability
    ):

        rankings = self.rank_agents()


        for agent in rankings:

            if capability.lower() in agent.lower():

                return agent


        return None