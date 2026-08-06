from __future__ import annotations

from core.knowledge.ux_pattern import UXPattern
from core.knowledge.ux_pattern import UXSection


AI_DASHBOARD = UXPattern(

    name="AI Dashboard",

    sections=[

        UXSection(
            "Header",
            [
                "Logo",
                "Search",
                "ProfileMenu",
            ],
        ),

        UXSection(
            "Sidebar",
            [
                "Navigation",
            ],
        ),

        UXSection(
            "Metrics",
            [
                "MetricCard",
                "MetricCard",
                "MetricCard",
            ],
        ),

        UXSection(
            "AI Workspace",
            [
                "ChatPanel",
                "PromptEditor",
            ],
        ),

        UXSection(
            "Footer",
            [
                "Footer",
            ],
        ),
    ],
)


PORTFOLIO = UXPattern(

    name="Portfolio",

    sections=[

        UXSection(
            "Hero",
            [
                "Headline",
                "CTA",
            ],
        ),

        UXSection(
            "Projects",
            [
                "ProjectCard",
            ],
        ),

        UXSection(
            "Timeline",
            [
                "Timeline",
            ],
        ),

        UXSection(
            "Footer",
            [
                "Footer",
            ],
        ),
    ],
)


UX_PATTERNS = {
    "ai_dashboard": AI_DASHBOARD,
    "portfolio": PORTFOLIO,
}
