from core.training.training_intelligence import TrainingIntelligence


REFERENCE = """
<div>
<Card>
Revenue
+18%
</Card>

<Sidebar>
Dashboard
Analytics
</Sidebar>

<Chart>
Growth
</Chart>

<Button>
Create
</Button>

</div>
"""


def test_component_roles_are_learned():

    profile = TrainingIntelligence().analyze(
        name="Dashboard Components",
        description="SaaS dashboard",
        code=REFERENCE,
    ).to_dict()

    roles = profile["component_roles"]

    assert roles["Card"]["role"] == "surface_container"
    assert roles["Sidebar"]["role"] == "navigation"
    assert roles["Chart"]["role"] == "visualization"
    assert roles["Button"]["role"] == "interaction"

    print(roles)
