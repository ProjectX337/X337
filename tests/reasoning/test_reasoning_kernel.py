from core.reasoning.reasoning_kernel import ReasoningKernel


def test_kernel():

    kernel = ReasoningKernel()

    kernel.vote(

        "SPA",

        weight=5,

        source="Intent",

        message="Dashboard",

    )

    kernel.vote(

        "SPA",

        weight=2,

        source="Capabilities",

        message="Analytics",

    )

    kernel.vote(

        "SSR",

        weight=3,

        source="Intent",

        message="SEO",

    )

    decision = kernel.resolve()

    assert decision.winner == "SPA"

    assert decision.confidence > 0.5

    assert len(decision.evidence) == 2

    assert len(decision.alternatives) == 1


if __name__ == "__main__":
    test_kernel()
    print("✅ ReasoningKernel passed")
