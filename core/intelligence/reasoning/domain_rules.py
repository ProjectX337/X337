from __future__ import annotations


DOMAIN_RULES = {
    "education": [
        "student",
        "students",
        "learning",
        "course",
        "teacher",
        "education",
        "tutor",
    ],

    "healthcare": [
        "patient",
        "doctor",
        "medical",
        "health",
        "clinic",
    ],

    "finance": [
        "bank",
        "payment",
        "invoice",
        "finance",
        "transaction",
    ],

    "ecommerce": [
        "store",
        "shop",
        "product",
        "checkout",
        "cart",
    ],
}


def infer_domain(text: str) -> str:

    text = text.lower()

    scores = {}

    for domain, keywords in DOMAIN_RULES.items():

        score = sum(
            keyword in text
            for keyword in keywords
        )

        if score:
            scores[domain] = score

    if not scores:
        return ""

    return max(
        scores,
        key=scores.get,
    )
