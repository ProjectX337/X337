from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ArchitectureRequirements:
    """
    Canonical engineering requirements derived from
    user intent and discovered product capabilities.

    This contract sits between product understanding
    and concrete architecture selection.
    """

    frontend: bool = False
    backend: bool = False
    ai: bool = False
    static_site: bool = False
    scripting: bool = False
    mobile: bool = False
    desktop: bool = False
    testing: bool = False

    required_roles: list[str] = field(
        default_factory=list
    )

    required_endpoints: list[str] = field(
        default_factory=list
    )

    required_capabilities: list[str] = field(
        default_factory=list
    )

    required_technologies: list[str] = field(
        default_factory=list
    )

    def require_role(self, role: str) -> None:
        role = role.strip().lower()

        if not role:
            return

        if role not in self.required_roles:
            self.required_roles.append(role)

        role_attribute_map = {
            "frontend": "frontend",
            "backend": "backend",
            "ai": "ai",
            "static_site": "static_site",
            "scripting": "scripting",
            "mobile": "mobile",
            "desktop": "desktop",
            "testing": "testing",
        }

        attribute = role_attribute_map.get(role)

        if attribute:
            setattr(self, attribute, True)

    def require_endpoint(self, endpoint: str) -> None:
        endpoint = endpoint.strip()

        if endpoint and endpoint not in self.required_endpoints:
            self.required_endpoints.append(endpoint)

    def require_capability(self, capability: str) -> None:
        capability = capability.strip().lower()

        if (
            capability
            and capability not in self.required_capabilities
        ):
            self.required_capabilities.append(
                capability
            )

    def require_technology(self, technology: str) -> None:
        technology = technology.strip().lower()

        if (
            technology
            and technology not in self.required_technologies
        ):
            self.required_technologies.append(
                technology
            )
