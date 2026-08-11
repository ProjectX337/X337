"""Compatibility facade for the canonical capability registry.

The canonical runtime registry is CapabilityRegistry from
core.capabilities.capability_registry.

This module preserves the older module-level API used by existing callers
while delegating all behavior to the canonical registry.
"""

from __future__ import annotations

from core.capabilities.capability import Capability
from core.capabilities.capability_registry import CapabilityRegistry


# Single canonical registry instance for legacy module-level callers.
_registry = CapabilityRegistry()


def get(name: str) -> Capability | None:
    """Return a capability by canonical name."""
    return _registry.get(name)


def all() -> list[Capability]:
    """Return all registered capabilities."""
    return _registry.all()


def names() -> list[str]:
    """Return all registered capability names."""
    return _registry.names()


def find_by_keyword(keyword: str) -> list[Capability]:
    """Return capabilities matching a keyword."""
    return _registry.find_by_keyword(keyword)


def match(prompt: str) -> list[Capability]:
    """Return capabilities relevant to a prompt.

    This compatibility API intentionally delegates matching to the canonical
    registry keyword index rather than maintaining a second registry.
    """
    text = prompt.lower()

    matches: list[Capability] = []
    seen: set[str] = set()

    for capability in _registry.all():
        if capability.name in seen:
            continue

        searchable = set(
            keyword.lower()
            for keyword in capability.keywords
        )

        searchable.add(capability.name.lower())

        if any(
            keyword in text
            for keyword in searchable
        ):
            matches.append(capability)
            seen.add(capability.name)

    return matches


# Compatibility alias for callers that expect a registry object.
registry = _registry


__all__ = [
    "Capability",
    "CapabilityRegistry",
    "registry",
    "get",
    "all",
    "names",
    "find_by_keyword",
    "match",
]
