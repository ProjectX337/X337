from core.planner.models import ParsedPrompt, Intent


class IntentClassifier:
    """
    Determines engineering intent from a parsed prompt.

    This stage decides WHAT the project needs,
    not HOW it will be built.
    """

    def classify(
        self,
        parsed: ParsedPrompt,
    ) -> Intent:

        text = parsed.original.lower()

        intent = Intent()

        # ----------------------------
        # Frontend
        # ----------------------------

        frontend_words = [
            "website",
            "landing",
            "frontend",
            "dashboard",
            "react",
            "ui",
            "interface",
            "portfolio",
            "blog",
            "page",
        ]

        if self._contains(text, frontend_words):
            intent.frontend = True

        # ----------------------------
        # Backend
        # ----------------------------

        backend_words = [
            "backend",
            "api",
            "server",
            "fastapi",
            "django",
            "flask",
            "authentication",
            "database",
            "crud",
        ]

        if self._contains(text, backend_words):
            intent.backend = True

        # ----------------------------
        # Database
        # ----------------------------

        database_words = [
            "database",
            "postgres",
            "postgresql",
            "mysql",
            "sqlite",
            "mongodb",
        ]

        if self._contains(text, database_words):
            intent.database = True

        # ----------------------------
        # Authentication
        # ----------------------------

        auth_words = [
            "authentication",
            "login",
            "signup",
            "jwt",
            "oauth",
            "users",
        ]

        if self._contains(text, auth_words):
            intent.authentication = True

        # ----------------------------
        # Deployment
        # ----------------------------

        deploy_words = [
            "docker",
            "deploy",
            "deployment",
            "kubernetes",
            "vercel",
            "railway",
        ]

        if self._contains(text, deploy_words):
            intent.deployment = True

        # ----------------------------
        # Testing
        # ----------------------------

        test_words = [
            "test",
            "tests",
            "testing",
            "pytest",
            "vitest",
        ]

        if self._contains(text, test_words):
            intent.testing = True

        # ----------------------------
        # Documentation
        # ----------------------------

        docs_words = [
            "documentation",
            "docs",
            "readme",
        ]

        if self._contains(text, docs_words):
            intent.documentation = True

        # ----------------------------
        # Dashboard
        # ----------------------------

        if "dashboard" in text:
            intent.dashboard = True

        # ----------------------------
        # API
        # ----------------------------

        if "api" in text:
            intent.api = True

        # ----------------------------
        # Website
        # ----------------------------

        if "website" in text or "landing page" in text:
            intent.website = True

        # ----------------------------
        # AI
        # ----------------------------

        ai_words = [
            "ai",
            "llm",
            "agent",
            "chatbot",
            "assistant",
            "openai",
        ]

        if self._contains(text, ai_words):
            intent.ai = True

        return intent

    # ------------------------------------

    def _contains(
        self,
        text,
        words,
    ):

        return any(
            word in text
            for word in words
        )