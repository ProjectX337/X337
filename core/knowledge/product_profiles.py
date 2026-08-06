from __future__ import annotations

from core.knowledge.product_profile import ProductProfile

AI_SAAS = ProductProfile(
    name="AI SaaS",
    description="Modern AI-powered SaaS platform.",

    layout="dashboard",
    theme="futuristic",
    navigation="sidebar",
    density="compact",
    motion="smooth",

    default_pages=[
        "Landing",
        "Dashboard",
        "Settings",
        "Billing",
        "API",
    ],

    default_components=[
        "Navbar",
        "Sidebar",
        "MetricCard",
        "DashboardCard",
        "DataTable",
        "ChatPanel",
        "CommandPalette",
    ],

    navigation_items=[
        "Dashboard",
        "AI",
        "Settings",
        "Billing",
    ],

    layout_sections=[
        "Hero",
        "Metrics",
        "Activity",
        "Sidebar",
        "Footer",
    ],

    required_features=[
        "authentication",
        "dashboard",
    ],

    recommended_capabilities=[
        "authentication",
        "analytics",
        "dashboard",
        "payments",
        "notifications",
        "search",
        "team_management",
        "crm",
        "ai",
    ],
)

PORTFOLIO = ProductProfile(
    name="Portfolio",
    description="Personal portfolio website.",

    layout="marketing",
    theme="modern",
    navigation="top",
    density="airy",
    motion="subtle",

    default_pages=[
        "Landing",
        "Projects",
        "About",
        "Contact",
    ],

    default_components=[
        "Navbar",
        "Hero",
        "ProjectCard",
        "Timeline",
        "Footer",
    ],

    navigation_items=[
        "Projects",
        "About",
        "Contact",
    ],

    layout_sections=[
        "Hero",
        "Projects",
        "Timeline",
        "Contact",
        "Footer",
    ],

    required_features=[],

    recommended_capabilities=[],
)

ENTERPRISE = ProductProfile(
    name="Enterprise",

    layout="dashboard",
    theme="modern",
    navigation="sidebar",
    density="compact",

    default_pages=[
        "Dashboard",
        "Users",
        "Reports",
        "Settings",
    ],

    default_components=[
        "Sidebar",
        "Navbar",
        "DataTable",
        "ReportCard",
    ],

    navigation_items=[
        "Dashboard",
        "Users",
        "Reports",
        "Settings",
    ],

    layout_sections=[
        "Header",
        "Content",
        "Sidebar",
        "Footer",
    ],

    required_features=[
        "authentication",
    ],

    recommended_capabilities=[
        "authentication",
        "analytics",
        "dashboard",
        "users",
        "reporting",
        "team_management",
    ],
)

PRODUCT_PROFILES = {
    "ai_saas": AI_SAAS,
    "portfolio": PORTFOLIO,
    "enterprise": ENTERPRISE,
}


def get_product_profile(name: str) -> ProductProfile:
    return PRODUCT_PROFILES[name]
