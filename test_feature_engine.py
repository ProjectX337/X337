from core.features.feature_engine import (
    FeatureEngine
)



engine = FeatureEngine()



features = engine.analyze(

"""
Create an AI tutor platform
with dyslexia_support
and adhd_support
"""

)



for feature in features:

    print("\nFEATURE")

    print(
        feature.name
    )


    print(
        "Pages:",
        feature.pages
    )


    print(
        "Components:",
        feature.components
    )


    print(
        "Services:",
        feature.services
    )


    print(
        "AI:",
        feature.ai_capabilities
    )