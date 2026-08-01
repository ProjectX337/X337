from __future__ import annotations

from core.capabilities.capability import Capability
from core.capabilities.capability_loader import CapabilityLoader


class CapabilityRegistry:
    """
    Central registry for all product capabilities.

    Builds indexes for fast lookup by
    - name
    - keyword
    """

    def __init__(self):

        self.loader = CapabilityLoader()

        self._capabilities: dict[str, Capability] = {}

        self._keyword_index: dict[str, list[Capability]] = {}

        self.reload()

    # ---------------------------------------------------------

    def reload(
        self,
    ) -> None:

        self._capabilities.clear()

        self._keyword_index.clear()

        for capability in self.loader.load():

            self._capabilities[
                capability.name
            ] = capability

            for keyword in capability.keywords:

                keyword = keyword.lower()

                self._keyword_index.setdefault(
                    keyword,
                    [],
                ).append(capability)

    # ---------------------------------------------------------

    def get(
        self,
        name: str,
    ) -> Capability | None:

        return self._capabilities.get(name)

    # ---------------------------------------------------------

    def names(
        self,
    ) -> list[str]:

        return sorted(
            self._capabilities.keys()
        )

    # ---------------------------------------------------------

    def all(
        self,
    ) -> list[Capability]:

        return list(
            self._capabilities.values()
        )

    # ---------------------------------------------------------

    def find_by_keyword(
        self,
        keyword: str,
    ) -> list[Capability]:

        return self._keyword_index.get(
            keyword.lower(),
            [],
        )

    # ---------------------------------------------------------

    def keyword_index(
        self,
    ) -> dict[str, list[Capability]]:

        return self._keyword_index
