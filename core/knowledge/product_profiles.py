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

    page_components={
        "Landing": [
            "Navbar",
            "ChatPanel",
        ],
        "Dashboard": [
            "Navbar",
            "Sidebar",
            "MetricCard",
            "DashboardCard",
            "DataTable",
        ],
        "Settings": [
            "Navbar",
            "Sidebar",
        ],
        "Billing": [
            "Navbar",
            "Sidebar",
        ],
        "API": [
            "Navbar",
            "Sidebar",
        ],
    },

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

    page_components={
        "Landing": [
            "Navbar",
            "Hero",
            "ProjectCard",
        ],
        "Projects": [
            "Navbar",
            "ProjectCard",
        ],
        "About": [
            "Navbar",
            "Timeline",
        ],
        "Contact": [
            "Navbar",
            "Footer",
        ],
    },

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

    page_components={
        "Dashboard": [
            "Sidebar",
            "Navbar",
            "DataTable",
            "ReportCard",
        ],
        "Users": [
            "Sidebar",
            "Navbar",
            "DataTable",
        ],
        "Reports": [
            "Sidebar",
            "Navbar",
            "ReportCard",
            "DataTable",
        ],
        "Settings": [
            "Sidebar",
            "Navbar",
        ],
    },

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

GENERIC_APPLICATION = ProductProfile(
    name="Generic Application",
    description="General-purpose application with adaptive UI structure.",
    layout="marketing",
    theme="modern",
    navigation="top",
    density="comfortable",
    motion="standard",
    default_pages=[
        "Landing",
    ],
    default_components=[
        "Navbar",
        "Hero",
        "Footer",
    ],
    page_components={
        "Landing": [
            "Navbar",
            "Hero",
            "Footer",
        ],
    },
    navigation_items=[],
    layout_sections=[
        "Header",
        "Content",
        "Footer",
    ],
    required_features=[],
    recommended_capabilities=[],
)


PRODUCT_PROFILES = {
    "ai_saas": AI_SAAS,
    "portfolio": PORTFOLIO,
    "enterprise": ENTERPRISE,
    "generic_application": GENERIC_APPLICATION,
}


def get_product_profile(name: str) -> ProductProfile:
    return PRODUCT_PROFILES[name]
