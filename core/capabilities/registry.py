from __future__ import annotations

from core.capabilities.models import Capability


class CapabilityRegistry:

    def __init__(self):
        self._capabilities: dict[str, Capability] = {}

    def register(self, capability: Capability):
        self._capabilities[capability.name] = capability

    def get(self, name: str):
        return self._capabilities.get(name)

    def all(self):
        return list(self._capabilities.values())

    def match(self, text: str):
        text = text.lower()

        matches = []

        for capability in self._capabilities.values():
            score = sum(
                keyword in text
                for keyword in capability.keywords
            )

            if score:
                matches.append((score, capability))

        matches.sort(key=lambda x: x[0], reverse=True)

        return [capability for _, capability in matches]
