from core.planner.feature_planner import (
    FeaturePlanner
)

from core.planner.models import (
    ParsedPrompt
)



planner = FeaturePlanner()



prompt = ParsedPrompt(

    original="""
    Create an AI tutor platform
    with dyslexia_support
    and adhd_support
    """

)



result = planner.plan(
    prompt
)



print("\nPAGES")

for page in result["pages"]:

    print(
        page.name,
        page.route
    )


print("\nCOMPONENTS")

for component in result["components"]:

    print(component)


print("\nSERVICES")

for service in result["services"]:

    print(service)