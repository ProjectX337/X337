from core.generators.base_generator import BaseGenerator
from core.generators.generation_result import GenerationResult
from core.generators.generator_registry import GeneratorRegistry


class DummyGenerator(BaseGenerator):

    @property
    def name(self):

        return "dummy"

    def generate(
        self,
        spec,
        step,
    ):

        return GenerationResult()


registry = GeneratorRegistry()

registry.register(
    DummyGenerator(),
)

print()

print("Registered Generators")

print("---------------------")

print(registry.names())

print()

print(

    registry.exists(
        "dummy",
    )

)

print(

    registry.get(
        "dummy",
    ).name

)
