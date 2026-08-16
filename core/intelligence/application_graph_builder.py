from core.graph.models import (
    GraphNode,
    GraphEdge,
    NodeKind,
    EdgeRelation,
)

from core.graph.models import ApplicationGraph

from core.intelligence.application_snapshot import (
    ApplicationSnapshot,
)


class ApplicationGraphBuilder:
    """
    Converts an ApplicationSnapshot
    into the canonical X337 application graph.
    """

    def build(
        self,
        snapshot: ApplicationSnapshot,
    ) -> ApplicationGraph:

        graph = ApplicationGraph()

        project_id = (
            f"project:{snapshot.project_name}"
        )

        graph.add_node(
            GraphNode(
                id=project_id,
                kind=NodeKind.PROJECT,
                name=snapshot.project_name,
            )
        )


        for file in snapshot.files:

            node_id = f"file:{file}"

            graph.add_node(
                GraphNode(
                    id=node_id,
                    kind=NodeKind.SOURCE_FILE,
                    name=file,
                )
            )

            graph.add_edge(
                GraphEdge(
                    source=project_id,
                    target=node_id,
                    relation=EdgeRelation.CONTAINS,
                )
            )


        if snapshot.framework:

            tech_id = (
                f"technology:{snapshot.framework}"
            )

            graph.add_node(
                GraphNode(
                    id=tech_id,
                    kind=NodeKind.TECHNOLOGY,
                    name=snapshot.framework,
                )
            )

            graph.add_edge(
                GraphEdge(
                    source=project_id,
                    target=tech_id,
                    relation=EdgeRelation.DEPENDS_ON,
                )
            )


        return graph
