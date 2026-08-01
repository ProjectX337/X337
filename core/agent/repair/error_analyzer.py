from __future__ import annotations


class ErrorAnalyzer:
    """
    Converts execution failures into repair tasks.
    """


    def analyze(
        self,
        result: dict,
    ):

        if result.get("passed"):

            return None


        output = result.get(
            "output",
            ""
        )


        return {
            "type": "test_failure",
            "message": output,
        }
