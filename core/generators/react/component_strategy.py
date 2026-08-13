from __future__ import annotations


def component_template_for(component) -> str:
    """
    Select component template from learned semantic metadata.
    """

    metadata = getattr(
        component,
        "metadata",
        {},
    ) or {}

    role = metadata.get(
        "training_role",
        "",
    )

    role_map = {
        "navigation": "react/components/navigation.tsx.j2",
        "visualization": "react/components/visualization.tsx.j2",
        "data": "react/components/table.tsx.j2",
        "form": "react/components/form.tsx.j2",
        "card": "react/components/card.tsx.j2",
        "interaction": "react/components/interaction.tsx.j2",
    }

    if role in role_map:
        return role_map[role]

    return "react/components/generic.tsx.j2"
