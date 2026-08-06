from __future__ import annotations

from core.knowledge.component_definition import ComponentDefinition


COMPONENTS = {

    "MetricCard": ComponentDefinition(

        name="MetricCard",

        children=[
            "Icon",
            "MetricValue",
            "Trend",
            "Sparkline",
        ],

    ),

    "DashboardCard": ComponentDefinition(

        name="DashboardCard",

        children=[
            "Header",
            "Content",
            "Footer",
        ],

    ),

    "ChatPanel": ComponentDefinition(

        name="ChatPanel",

        children=[
            "Conversation",
            "PromptInput",
            "Toolbar",
        ],

    ),

    "Sidebar": ComponentDefinition(

        name="Sidebar",

        children=[
            "Logo",
            "Navigation",
            "Footer",
        ],

    ),

}
