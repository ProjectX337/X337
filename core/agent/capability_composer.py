from __future__ import annotations


class CapabilityComposer:
    """
    Converts high-level product concepts
    into composed feature sets.
    """

    CAPABILITIES = {

        "saas_admin": [
            "authentication",
            "billing",
            "dashboard",
            "analytics",
        ],

        "customer_portal": [
            "authentication",
            "dashboard",
        ],

        "analytics_platform": [
            "authentication",
            "dashboard",
            "analytics",
        ],

    }


    def compose(
        self,
        message: str,
    ) -> list[str]:

        text = message.lower()

        features = []

        for capability, items in self.CAPABILITIES.items():

            words = capability.replace("_", " ").split()

            score = 0

            for word in words:

                if word in text:
                    score += 1

            if score == len(words):

                features.extend(items)


        return list(dict.fromkeys(features))
