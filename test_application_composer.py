from core.planner.application_composer import (
    ApplicationComposer
)

from core.planner.models import (
    ParsedPrompt
)



composer = ApplicationComposer()



prompt = ParsedPrompt(

original="""
Create an AI tutor platform
with dyslexia_support
and adhd_support
"""

)



app = composer.compose(
    prompt
)



print("\nAPPLICATION")

print(
    app.name
)


print("\nFEATURES")

for feature in app.features:

    print(feature)



print("\nPAGES")

for page in app.pages:

    print(
        page.name,
        page.route
    )



print("\nCOMPONENTS")

for component in app.components:

    print(component)



print("\nSERVICES")

for service in app.services:

    print(service)