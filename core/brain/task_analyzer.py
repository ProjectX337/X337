class TaskAnalyzer:


    def analyze(
        self,
        task
    ):


        title = task.title.lower()


        requirements = []



        #
        # Determine category
        #

        category = "general"



        if any(
            word in title
            for word in [
                "python",
                "code",
                "software",
                "app",
                "application",
                "website",
                "program",
                "script",
                "api",
                "build"
            ]
        ):

            category = "software"



        if any(
            word in title
            for word in [
                "tutor",
                "education",
                "course",
                "lesson",
                "learning",
                "teacher"
            ]
        ):

            category = "education"



        if any(
            word in title
            for word in [
                "data",
                "dataset",
                "analytics",
                "customer",
                "statistics"
            ]
        ):

            category = "data_analysis"



        if any(
            word in title
            for word in [
                "research",
                "study",
                "investigate",
                "explore"
            ]
        ):

            category = "research"



        #
        # Capability detection
        #



        if any(
            word in title
            for word in [
                "research",
                "analyze",
                "study",
                "investigate",
                "explore"
            ]
        ):

            requirements.append(
                "research"
            )



        if any(
            word in title
            for word in [
                "write",
                "document",
                "article",
                "report",
                "summary",
                "essay"
            ]
        ):

            requirements.append(
                "writing"
            )



        if any(
            word in title
            for word in [
                "code",
                "coding",
                "python",
                "program",
                "software",
                "app",
                "application",
                "website",
                "script",
                "build",
                "api"
            ]
        ):

            requirements.append(
                "coding"
            )



        #
        # Education tasks benefit from writing/research
        #

        if category == "education":

            requirements.extend(

                [
                    "research",
                    "writing",
                    "coding"
                ]

            )



        #
        # Data tasks need research + coding
        #

        if category == "data_analysis":

            requirements.extend(

                [
                    "research",
                    "coding"
                ]

            )



        #
        # Software receives testing
        #

        if "coding" in requirements:

            requirements.append(
                "testing"
            )



        #
        # Every workflow receives review
        #

        requirements.append(
            "review"
        )



        #
        # Remove duplicates
        #

        requirements = list(

            dict.fromkeys(

                requirements

            )

        )



        return {

            "category": category,

            "capabilities": requirements

        }