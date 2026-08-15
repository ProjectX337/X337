from core.cognition.cognitive_state import CognitiveState


def test_cognitive_state():

    state = CognitiveState(
        prompt="Build an AI SaaS"
    )

    assert state.prompt == "Build an AI SaaS"

    assert state.application_graph is not None


if __name__ == "__main__":
    test_cognitive_state()
    print("✅ CognitiveState passed")
