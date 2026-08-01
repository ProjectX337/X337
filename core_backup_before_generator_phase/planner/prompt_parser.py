import re

from core.planner.models import ParsedPrompt


class PromptParser:
    """
    Parses a natural language prompt into
    structured information.

    This stage does NOT decide technologies.
    It simply extracts information.
    """

    PROJECT_TYPES = [
        "website",
        "landing page",
        "dashboard",
        "crm",
        "api",
        "backend",
        "frontend",
        "portfolio",
        "blog",
        "ecommerce",
        "store",
        "marketplace",
        "saas",
        "ai agent",
        "chatbot",
    ]

    STYLES = [
        "modern",
        "minimal",
        "luxury",
        "premium",
        "glassmorphism",
        "apple",
        "stripe",
        "dark",
        "light",
        "corporate",
        "futuristic",
    ]

    DOMAINS = [
        "healthcare",
        "finance",
        "legal",
        "education",
        "real estate",
        "restaurant",
        "fitness",
        "ai",
        "technology",
        "travel",
        "gaming",
        "ecommerce",
    ]

    def parse(self, prompt: str) -> ParsedPrompt:

        text = prompt.strip()

        parsed = ParsedPrompt(
            original=text,
            description=text,
        )

        lower = text.lower()

        parsed.project_type = self._find_match(
            lower,
            self.PROJECT_TYPES,
        )

        parsed.style = self._find_match(
            lower,
            self.STYLES,
        )

        parsed.domain = self._find_match(
            lower,
            self.DOMAINS,
        )

        parsed.project_name = self._extract_name(text)

        parsed.keywords = self._keywords(lower)

        return parsed

    def _find_match(
        self,
        text,
        options,
    ):

        for option in options:

            if option in text:
                return option

        return ""

    def _extract_name(
        self,
        prompt,
    ):

        patterns = [

            r"called\s+([A-Za-z0-9_-]+)",

            r"named\s+([A-Za-z0-9_-]+)",

            r"for\s+([A-Za-z0-9_-]+)",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                prompt,
                re.IGNORECASE,
            )

            if match:
                return match.group(1)

        return ""

    def _keywords(
        self,
        text,
    ):

        words = re.findall(
            r"[A-Za-z]{3,}",
            text,
        )

        stop_words = {

            "build",
            "create",
            "make",
            "with",
            "using",
            "that",
            "this",
            "into",
            "from",
            "have",
            "website",
            "application",
            "project",
        }

        keywords = []

        for word in words:

            if word in stop_words:
                continue

            if word not in keywords:
                keywords.append(word)

        return keywords