class TaskAnalyzer:


    def analyze(self, task):

        text = task.title.lower()


        if any(
            word in text
            for word in [
                "website",
                "web app",
                "frontend"
            ]
        ):

            return "web_development"


        if any(
            word in text
            for word in [
                "csv",
                "data",
                "analysis",
                "report"
            ]
        ):

            return "data_analysis"


        if any(
            word in text
            for word in [
                "ai agent",
                "agent",
                "assistant"
            ]
        ):

            return "agent_development"


        if any(
            word in text
            for word in [
                "research",
                "study",
                "compare"
            ]
        ):

            return "research"


        return "general_coding"