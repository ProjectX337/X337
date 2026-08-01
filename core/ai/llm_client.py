from __future__ import annotations


class LLMClient:
    """
    Interface for language model providers.
    """

    def complete(
        self,
        prompt: str,
    ) -> str:

        raise NotImplementedError
