"""
X337 canonical capability package.

Capability definitions are loaded through CapabilityRegistry.
The package initializer intentionally performs no registration
and imports no legacy capability models.
"""

from core.capabilities.capability import Capability
from core.capabilities.capability_registry import CapabilityRegistry

__all__ = [
    "Capability",
    "CapabilityRegistry",
]
