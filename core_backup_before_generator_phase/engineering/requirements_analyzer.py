from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ProjectRequirements:
    """
    Structured engineering requirements extracted
    from a natural-language task.
    """

    project_type: str = "python"

    frontend: bool = False

    backend: bool = False

    api: bool = False

    website: bool = False

    desktop: bool = False

    mobile: bool = False

    database: bool = False

    authentication: bool = False

    testing: bool = True

    deployment: bool = False

    docker: bool = False

    ci_cd: bool = False

    documentation: bool = True

    ai: bool = False

    realtime: bool = False

    features: list[str] = field(default_factory=list)


class RequirementsAnalyzer:
    """
    Converts natural language tasks into
    structured engineering requirements.
    """

    def analyze(
        self,
        task: str
    ) -> ProjectRequirements:

        text = task.lower()

        requirements = ProjectRequirements()

        # ----------------------------
        # Project Type
        # ----------------------------

        if "website" in text:

            requirements.project_type = "website"

            requirements.website = True

            requirements.frontend = True

        elif "api" in text:

            requirements.project_type = "fastapi"

            requirements.backend = True

            requirements.api = True

        elif "agent" in text:

            requirements.project_type = "ai_agent"

            requirements.ai = True

        elif "desktop" in text:

            requirements.project_type = "desktop"

            requirements.desktop = True

        elif "mobile" in text:

            requirements.project_type = "mobile"

            requirements.mobile = True

        # ----------------------------
        # Authentication
        # ----------------------------

        auth_keywords = [

            "login",

            "authentication",

            "auth",

            "oauth",

            "jwt",

            "user accounts"

        ]

        if any(word in text for word in auth_keywords):

            requirements.authentication = True

            requirements.features.append("authentication")

        # ----------------------------
        # Database
        # ----------------------------

        database_keywords = [

            "database",

            "sqlite",

            "postgres",

            "mysql",

            "users",

            "storage"

        ]

        if any(word in text for word in database_keywords):

            requirements.database = True

        # ----------------------------
        # Docker
        # ----------------------------

        if "docker" in text:

            requirements.docker = True

            requirements.deployment = True

        # ----------------------------
        # CI/CD
        # ----------------------------

        ci_keywords = [

            "github actions",

            "ci",

            "pipeline"

        ]

        if any(word in text for word in ci_keywords):

            requirements.ci_cd = True

        # ----------------------------
        # AI
        # ----------------------------

        ai_keywords = [

            "ai",

            "llm",

            "chatgpt",

            "openai"

        ]

        if any(word in text for word in ai_keywords):

            requirements.ai = True

        # ----------------------------
        # Realtime
        # ----------------------------

        realtime_keywords = [

            "chat",

            "websocket",

            "stream"

        ]

        if any(word in text for word in realtime_keywords):

            requirements.realtime = True

        return requirements