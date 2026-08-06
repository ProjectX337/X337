from __future__ import annotations

from core.capabilities.authentication import create_capability
from core.capabilities.registry import CapabilityRegistry

registry = CapabilityRegistry()
registry.register(create_capability())
