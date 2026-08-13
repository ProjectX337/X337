from __future__ import annotations


WORKFLOW_RULES = {

    "learning assistant": [
        "student asks question",
        "assistant explains concept",
        "student reviews answer",
        "progress is tracked",
    ],

    "chatbot": [
        "user sends message",
        "assistant generates response",
    ],

    "dashboard": [
        "user views metrics",
        "user analyzes information",
    ],

}


def infer_workflows(text: str) -> list[str]:

    text = text.lower()

    workflows = []

    for pattern, steps in WORKFLOW_RULES.items():

        if pattern in text:

            workflows.extend(
                steps
            )

    return workflows
