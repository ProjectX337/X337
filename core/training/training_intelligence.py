from __future__ import annotations

import re
from collections import Counter
from dataclasses import asdict, dataclass, field


@dataclass
class TrainingProfile:
    """
    Structured knowledge extracted from a submitted reference.

    This is intentionally deterministic and local. It does not
    blindly copy submitted source code into future generations.
    """

    visual_style: str = ""
    frameworks: list[str] = field(default_factory=list)
    libraries: list[str] = field(default_factory=list)

    colors: list[str] = field(default_factory=list)

    color_roles: dict[str, list[str]] = field(
        default_factory=dict
    )

    fonts: list[str] = field(default_factory=list)

    spacing_values: list[str] = field(default_factory=list)
    spacing_roles: dict[str, list[str]] = field(
        default_factory=dict
    )
    radius_values: list[str] = field(default_factory=list)

    layout_patterns: list[str] = field(default_factory=list)
    component_patterns: list[str] = field(default_factory=list)

    component_roles: dict[str, dict] = field(
        default_factory=dict
    )
    interaction_patterns: list[str] = field(default_factory=list)

    css_class_patterns: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    confidence: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)


class TrainingIntelligence:
    """
    Extracts reusable implementation and design signals from
    reference code.

    The goal is style adoption, not source-code memorization.
    """

    COLOR_RE = re.compile(
        r"#[0-9a-fA-F]{3,8}\b"
        r"|rgba?\([^)]*\)"
        r"|hsla?\([^)]*\)"
    )

    PX_RE = re.compile(
        r"\b\d+(?:\.\d+)?(?:px|rem|em|vh|vw|%)\b"
    )

    FONT_RE = re.compile(
        r"font-family\s*:\s*([^;}{]+)"
        r"|fontFamily\s*:\s*[\"']?([^,;}\"']+)"
    )

    CLASS_RE = re.compile(
        r'className\s*=\s*[{"\']([^"}\']+)',
        re.MULTILINE,
    )

    IMPORT_RE = re.compile(
        r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]'
    )

    JSX_TAG_RE = re.compile(
        r"<([A-Z][A-Za-z0-9_]*)"
    )

    def analyze(
        self,
        *,
        name: str,
        description: str,
        code: str,
    ) -> TrainingProfile:

        code = code or ""
        description = description or ""

        profile = TrainingProfile()

        imports = self.IMPORT_RE.findall(code)

        for item in imports:
            lower = item.lower()

            if "react" in lower:
                profile.frameworks.append("react")

            if "next" in lower:
                profile.frameworks.append("nextjs")

            if "vue" in lower:
                profile.frameworks.append("vue")

            if "svelte" in lower:
                profile.frameworks.append("svelte")

            for library in (
                "framer-motion",
                "lucide-react",
                "three",
                "react-three-fiber",
                "zustand",
                "tailwind",
                "radix",
                "shadcn",
            ):
                if library in lower:
                    profile.libraries.append(library)

        profile.colors = self._top_values(
            self.COLOR_RE.findall(code),
            limit=12,
        )

        profile.color_roles = self._extract_color_roles(
            code
        )

        fonts = []

        for match in self.FONT_RE.findall(code):
            fonts.extend(
                value.strip()
                for value in match
                if value.strip()
            )

        profile.fonts = self._top_values(
            fonts,
            limit=8,
        )

        # -----------------------------------------------------
        # Property-aware dimensional extraction
        # -----------------------------------------------------

        declaration_re = re.compile(
            r"(?P<property>[A-Za-z-]+)\s*:\s*"
            r"(?P<value>[^;{}\n]+)"
        )

        declarations = declaration_re.findall(code)

        spacing_properties = {
            "padding",
            "padding-top",
            "padding-right",
            "padding-bottom",
            "padding-left",
            "margin",
            "margin-top",
            "margin-right",
            "margin-bottom",
            "margin-left",
            "gap",
            "row-gap",
            "column-gap",
        }

        radius_properties = {
            "border-radius",
            "border-top-left-radius",
            "border-top-right-radius",
            "border-bottom-left-radius",
            "border-bottom-right-radius",
        }

        spacing_values = []
        radius_values = []

        for property_name, value in declarations:
            property_name = property_name.strip().lower()

            extracted = self.PX_RE.findall(value)

            if property_name in spacing_properties:
                spacing_values.extend(extracted)

            elif property_name in radius_properties:
                radius_values.extend(extracted)

        profile.spacing_values = self._top_values(
            spacing_values,
            limit=12,
        )

        profile.radius_values = self._top_values(
            radius_values,
            limit=8,
        )

        profile.spacing_roles = {
            "compact": self._top_values(
                [
                    value
                    for value in spacing_values
                    if self._numeric(value) <= 16
                ],
                limit=8,
            ),
            "comfortable": self._top_values(
                [
                    value
                    for value in spacing_values
                    if 16 < self._numeric(value) <= 32
                ],
                limit=8,
            ),
            "spacious": self._top_values(
                [
                    value
                    for value in spacing_values
                    if self._numeric(value) > 32
                ],
                limit=8,
            ),
        }

        classes = self.CLASS_RE.findall(code)

        class_tokens = []

        for value in classes:
            class_tokens.extend(
                token
                for token in re.split(
                    r"\s+",
                    value.strip(),
                )
                if token
            )

        profile.css_class_patterns = self._top_values(
            class_tokens,
            limit=20,
        )

        jsx_components = self.JSX_TAG_RE.findall(code)

        known_components = {
            "Button",
            "Card",
            "Modal",
            "Dialog",
            "Sidebar",
            "Navbar",
            "Header",
            "Footer",
            "Table",
            "Chart",
            "Input",
            "Textarea",
            "Form",
            "Avatar",
            "Badge",
            "Tabs",
            "Tooltip",
            "Dropdown",
            "Command",
        }

        profile.component_patterns = self._top_values(
            [
                component
                for component in jsx_components
                if component in known_components
            ],
            limit=20,
        )


        component_patterns = profile.component_patterns

        component_roles = {}

        role_keywords = {
            "Card": {
                "role": "surface_container",
                "signals": [
                    "metric",
                    "value",
                    "label",
                    "trend",
                ],
            },
            "Chart": {
                "role": "visualization",
                "signals": [
                    "data",
                    "growth",
                    "analytics",
                ],
            },
            "Sidebar": {
                "role": "navigation",
                "signals": [
                    "menu",
                    "links",
                    "navigation",
                ],
            },
            "Navbar": {
                "role": "top_navigation",
                "signals": [
                    "brand",
                    "actions",
                    "navigation",
                ],
            },
            "Button": {
                "role": "interaction",
                "signals": [
                    "action",
                    "submit",
                    "create",
                ],
            },
        }

        for component in component_patterns:
            if component in role_keywords:
                component_roles[component] = role_keywords[component]

        profile.component_roles = component_roles

        layout_rules = (
            {
                "grid":
                    r"\bgrid\b|display\s*:\s*grid",
                "flex":
                    r"\bflex\b|display\s*:\s*flex",
                "sidebar":
                    r"\bsidebar\b",
                "responsive":
                    r"@media|max-width|min-width|responsive",
                "cards":
                    r"\bcard\b|card-",
                "dashboard":
                    r"\bdashboard\b",
                "glass":
                    r"backdrop-filter|backdrop-blur|rgba\(",
                "gradient":
                    r"linear-gradient|radial-gradient",
                "dark":
                    r"#0[0-9a-fA-F]{1,6}|#1[0-9a-fA-F]{1,6}",
            }
        )

        for pattern_name, pattern in layout_rules.items():
            if re.search(
                pattern,
                code,
                re.IGNORECASE,
            ):
                profile.layout_patterns.append(
                    pattern_name
                )

        interactions = {
            "forms": r"<form|onSubmit|handleSubmit",
            "buttons": r"<button|onClick",
            "inputs": r"<input|<textarea|<select",
            "animation": r"motion\.|animate-|transition-|framer-motion",
            "drag": r"drag[A-Z]|draggable",
            "modal": r"Modal|Dialog",
            "navigation": r"navigate\(|Link|router",
        }

        for pattern_name, pattern in interactions.items():
            if re.search(
                pattern,
                code,
                re.IGNORECASE,
            ):
                profile.interaction_patterns.append(
                    pattern_name
                )

        text = (
            f"{name} "
            f"{description} "
            f"{code[:12000]}"
        ).lower()

        visual_keywords = [
            "futuristic",
            "minimal",
            "modern",
            "dark",
            "light",
            "glass",
            "glassmorphism",
            "dashboard",
            "saas",
            "editorial",
            "luxury",
            "playful",
            "enterprise",
            "gradient",
            "responsive",
            "clean",
            "professional",
        ]

        profile.keywords = [
            keyword
            for keyword in visual_keywords
            if keyword in text
        ]

        style_tokens = []

        if "dark" in profile.keywords:
            style_tokens.append("dark")

        if "glass" in profile.layout_patterns:
            style_tokens.append("glassmorphism")

        if "gradient" in profile.layout_patterns:
            style_tokens.append("gradient")

        if "dashboard" in profile.layout_patterns:
            style_tokens.append("dashboard")

        if "responsive" in profile.layout_patterns:
            style_tokens.append("responsive")

        if not style_tokens:
            style_tokens.append("modern")

        profile.visual_style = " ".join(
            dict.fromkeys(style_tokens)
        )

        profile.frameworks = self._unique(
            profile.frameworks
        )

        profile.libraries = self._unique(
            profile.libraries
        )

        profile.layout_patterns = self._unique(
            profile.layout_patterns
        )

        profile.component_patterns = self._unique(
            profile.component_patterns
        )

        profile.interaction_patterns = self._unique(
            profile.interaction_patterns
        )

        profile.keywords = self._unique(
            profile.keywords
        )

        signal_count = sum(
            bool(value)
            for value in (
                profile.frameworks,
                profile.libraries,
                profile.colors,
                profile.fonts,
                profile.layout_patterns,
                profile.component_patterns,
                profile.interaction_patterns,
                profile.keywords,
            )
        )

        profile.confidence = min(
            1.0,
            0.2 + signal_count * 0.08,
        )

        return profile

    def _extract_color_roles(
        self,
        code: str,
    ) -> dict[str, list[str]]:
        """
        Infer semantic color roles from CSS selector/property context.
        """

        roles = {
            "background": [],
            "surface": [],
            "primary": [],
            "secondary": [],
            "accent": [],
            "text": [],
            "muted": [],
            "border": [],
        }

        block_re = re.compile(
            r"(?P<selector>[^{}]+)\{(?P<body>[^{}]*)\}",
            re.MULTILINE,
        )

        declaration_re = re.compile(
            r"(?P<property>[A-Za-z-]+)\s*:\s*"
            r"(?P<value>[^;{}\n]+)",
        )

        for block in block_re.finditer(code):
            selector = block.group("selector").strip().lower()
            body = block.group("body")

            for declaration in declaration_re.finditer(body):
                property_name = (
                    declaration.group("property")
                    .strip()
                    .lower()
                )

                value = declaration.group("value").strip()

                colors = self.COLOR_RE.findall(value)

                for color in colors:
                    if property_name in {
                        "background",
                        "background-color",
                    }:
                        if any(
                            token in selector
                            for token in (
                                ":root",
                                "body",
                                "html",
                                "app",
                                "page",
                                "shell",
                                "dashboard",
                            )
                        ):
                            roles["background"].append(color)

                        elif any(
                            token in selector
                            for token in (
                                "card",
                                "panel",
                                "surface",
                                "sidebar",
                                "modal",
                                "dialog",
                            )
                        ):
                            roles["surface"].append(color)

                        elif any(
                            token in selector
                            for token in (
                                "primary",
                                "accent",
                                "button",
                                "btn",
                                "cta",
                                "action",
                            )
                        ):
                            roles["primary"].append(color)
                            roles["accent"].append(color)

                        else:
                            roles["surface"].append(color)

                    elif property_name == "color":
                        if any(
                            token in selector
                            for token in (
                                "muted",
                                "secondary",
                                "subtitle",
                                "description",
                                "caption",
                                "small",
                            )
                        ):
                            roles["muted"].append(color)

                        else:
                            roles["text"].append(color)

                    elif property_name in {
                        "border",
                        "border-color",
                        "outline",
                        "outline-color",
                    }:
                        roles["border"].append(color)

        # -----------------------------------------------------
        # React inline style support
        # -----------------------------------------------------

        inline_re = re.compile(
            r"(?P<property>"
            r"background|backgroundColor|"
            r"color|borderColor|border"
            r")"
            r"\s*:\s*[\"']?"
            r"(?P<value>[^,}\"]+)",
        )

        for match in inline_re.finditer(code):
            property_name = (
                match.group("property")
                .lower()
            )

            value = match.group("value").strip()

            colors = self.COLOR_RE.findall(value)

            for color in colors:
                if "background" in property_name:
                    roles["surface"].append(color)

                elif property_name == "color":
                    roles["text"].append(color)

                else:
                    roles["border"].append(color)

        return {
            role: self._top_values(
                values,
                limit=8,
            )
            for role, values in roles.items()
            if values
        }

    @staticmethod
    def _unique(values: list[str]) -> list[str]:
        return list(
            dict.fromkeys(
                value
                for value in values
                if value
            )
        )

    @staticmethod
    def _numeric(value: str) -> float:
        match = re.search(
            r"-?\d+(?:\.\d+)?",
            str(value),
        )

        if not match:
            return 0.0

        return float(match.group(0))

    @staticmethod
    def _top_values(
        values: list[str],
        *,
        limit: int,
    ) -> list[str]:
        counter = Counter(values)

        return [
            value
            for value, _count in counter.most_common(limit)
        ]
