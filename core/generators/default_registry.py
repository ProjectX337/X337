from __future__ import annotations

from core.generators.generator_registry import GeneratorRegistry

from core.generators.react.generator import ReactGenerator
from core.generators.ai.generator import AIAgentGenerator
from core.generators.python.generator import PythonGenerator


def create_default_registry() -> GeneratorRegistry:

    registry = GeneratorRegistry()

    registry.register(
        ReactGenerator()
    )

    registry.register(
        AIAgentGenerator()
    )

    registry.register(
        PythonGenerator()
    )

    return registry
