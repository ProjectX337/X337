from core.planner.application_composer import (
    ApplicationComposer
)

from core.planner.application_adapter import (
    ApplicationAdapter
)

from core.planner.models import (
    ParsedPrompt
)

from core.generator.react_generator import (
    ReactGenerator
)



prompt = ParsedPrompt(

original="""
Create an AI tutor platform
with dyslexia_support
and adhd_support
"""

)



composer = ApplicationComposer()


application = composer.compose(
    prompt
)



adapter = ApplicationAdapter()


blueprint = adapter.convert(
    application
)



generator = ReactGenerator()


result = generator.generate(
    blueprint
)


print(result)