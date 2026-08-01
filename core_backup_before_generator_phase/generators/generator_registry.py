from __future__ import annotations

from core.generators.base_generator import BaseGenerator


class GeneratorRegistry:
    """
    Registry of all available generators.
    """

    def __init__(self):

        self._generators: dict[str, BaseGenerator] = {}

    # ---------------------------------------------------------

    def register(
        self,
        generator: BaseGenerator,
    ) -> None:

        self._generators[
            generator.name
        ] = generator

    # ---------------------------------------------------------

    def get(
        self,
        name: str,
    ) -> BaseGenerator:

        try:

            return self._generators[name]

        except KeyError:

            raise ValueError(

                f"No generator registered "

                f"for '{name}'."

            ) from None

    # ---------------------------------------------------------

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._generators

    # ---------------------------------------------------------

    def names(
        self,
    ) -> list[str]:

        return sorted(
            self._generators.keys(),
        )
