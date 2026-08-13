from core.execution.capabilities.apply_feature_change import (
    ApplyFeatureChangeCapability,
)

from core.spec.project_spec import ProjectSpec


class DummyPlan:

    feature = "auth"

    routes = ["/login"]
    pages = ["Login"]
    components = ["LoginForm"]
    state = ["authenticated"]
    api_contracts = ["POST /login"]



class DummyTask:

    metadata = {
        "project": ProjectSpec(),
        "plan": DummyPlan(),
    }



def test_apply_feature_change_adds_feature():

    capability = ApplyFeatureChangeCapability()

    result = capability.execute(
        DummyTask()
    )

    assert result.success is True

    assert (
        DummyTask.metadata["project"]
        .feature_models[0]
        .name
        == "auth"
    )
