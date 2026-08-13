from __future__ import annotations


QUALITY_RULES = {

    "healthcare": [
        "secure",
        "privacy-focused",
        "reliable",
    ],

    "finance": [
        "secure",
        "auditable",
        "accurate",
    ],

    "education": [
        "personalized",
        "adaptive",
        "engaging",
    ],

    "ai": [
        "explainable",
        "adaptive",
    ],

}


def infer_quality_attributes(
    text: str,
    domain: str,
) -> list[str]:

    attributes = set()

    text = text.lower()

    for key, values in QUALITY_RULES.items():

        if key in text or key == domain:

            attributes.update(
                values
            )

    return sorted(attributes)
