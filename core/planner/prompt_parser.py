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

    TECHNOLOGIES = [
        "ai",
        "llm",
        "openai",
        "machine learning",
        "blockchain",
        "cloud",
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

        parsed.domain = self._find_domain(
            lower,
        )

        parsed.technologies = self._matches(
            lower,
            self.TECHNOLOGIES,
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

    def _find_domain(
        self,
        text,
    ):

        for domain in self.DOMAINS:

            if domain == "ai":
                continue

            if domain in text:
                return domain

        return ""

    def _matches(
        self,
        text,
        options,
    ):

        matches = []

        for option in options:

            if option in text:
                matches.append(option)

        return matches

    def _extract_name(
        self,
        prompt,
    ):
        """
        Extract an explicit product name or infer a meaningful
        product identity from the opening product description.
        """

        explicit_patterns = [
            r"called\s+([A-Za-z0-9_-]+)",
            r"named\s+([A-Za-z0-9_-]+)",
        ]

        for pattern in explicit_patterns:
            match = re.search(
                pattern,
                prompt,
                re.IGNORECASE,
            )

            if match:
                return match.group(1)

        match = re.search(
            r"^(?:build|create|make|develop|design)\s+(.+)$",
            prompt.strip(),
            re.IGNORECASE,
        )

        if not match:
            return ""

        description = match.group(1).strip()

        # Remove leading article only.
        description = re.sub(
            r"^(?:a|an|the)\s+",
            "",
            description,
            flags=re.IGNORECASE,
        )

        # Keep the complete product phrase when it ends in a
        # generic product-type noun.
        generic_suffixes = (
            "application",
            "app",
            "platform",
            "system",
            "tool",
            "software",
            "website",
            "dashboard",
            "portal",
        )

        words = description.split()

        # Find the first generic product noun and retain the
        # meaningful phrase immediately before it.
        for index, word in enumerate(words):
            normalized = re.sub(
                r"[^A-Za-z0-9_-]",
                "",
                word,
            ).lower()

            if normalized in generic_suffixes:
                meaningful = words[:index]

                if meaningful:
                    return "-".join(
                        re.sub(
                            r"[^A-Za-z0-9_-]",
                            "",
                            value,
                        )
                        for value in meaningful
                    )

                return normalized

        # No generic suffix: stop before common requirement clauses.
        words = re.split(
            r"\s+(?:with|using|for|that|which|including)\s+",
            description,
            maxsplit=1,
            flags=re.IGNORECASE,
        )[0].strip()

        tokens = re.findall(
            r"[A-Za-z0-9_-]+",
            words,
        )

        return "-".join(tokens[:8])

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