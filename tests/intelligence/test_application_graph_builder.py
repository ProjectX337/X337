from core.intelligence.application_snapshot import (
    ApplicationSnapshot,
)

from core.intelligence.application_graph_builder import (
    ApplicationGraphBuilder,
)


def test_application_graph_builder():

    snapshot = ApplicationSnapshot(
        project_name="demo",
        root_path="/tmp/demo",
        framework="javascript",
        files=[
            "package.json",
            "src/App.tsx",
        ],
    )

    graph = ApplicationGraphBuilder().build(
        snapshot
    )

    nodes = graph.nodes

    assert (
        "project:demo"
        in nodes
    )

    assert (
        "file:src/App.tsx"
        in nodes
    )
