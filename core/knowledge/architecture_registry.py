from __future__ import annotations

from core.knowledge.architecture_definition import ArchitectureDefinition


SPA = ArchitectureDefinition(

    name="SPA",

    routing="client",

    state="zustand",

    rendering="csr",

    api_style="rest",

    deployment="static",

    recommended_components=[
        "Sidebar",
        "Navbar",
        "CommandPalette",
    ],

    recommended_patterns=[
        "Dashboard",
        "Settings",
    ],
)

SSR = ArchitectureDefinition(

    name="SSR",

    routing="server",

    state="server",

    rendering="ssr",

    api_style="rest",

    deployment="edge",

    recommended_components=[
        "Hero",
        "Footer",
    ],

    recommended_patterns=[
        "Marketing",
        "Landing",
    ],
)

ARCHITECTURES = {
    "SPA": SPA,
    "SSR": SSR,
}
