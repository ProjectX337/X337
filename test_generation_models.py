from core.generators.generated_file import GeneratedFile
from core.generators.generation_result import GenerationResult

result = GenerationResult()

result.add_file(

    GeneratedFile(

        path="frontend/package.json",

        content='{"name":"frontend"}',

        language="json",

    )

)

print(result)
