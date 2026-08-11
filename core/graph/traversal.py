from __future__ import annotations

from collections import deque

from core.graph.models import ApplicationGraph, GraphNode


class GraphTraversal:
    """
    Graph traversal utilities operating on the canonical graph API.
    """

    def __init__(self, graph: ApplicationGraph):
        self.graph = graph

    def bfs(
        self,
        start: str,
    ) -> list[GraphNode]:

        visited: set[str] = set()
        queue = deque([start])
        order: list[GraphNode] = []

        while queue:

            node_id = queue.popleft()

            if node_id in visited:
                continue

            visited.add(node_id)

            if not self.graph.has_node(node_id):
                continue

            node = self.graph.get(node_id)
            order.append(node)

            for neighbor in self.graph.neighbors(node_id):

                if neighbor.id not in visited:
                    queue.append(neighbor.id)

        return order

    def dfs(
        self,
        start: str,
    ) -> list[GraphNode]:

        visited: set[str] = set()
        order: list[GraphNode] = []

        def visit(node_id: str) -> None:

            if node_id in visited:
                return

            visited.add(node_id)

            if not self.graph.has_node(node_id):
                return

            node = self.graph.get(node_id)
            order.append(node)

            for neighbor in self.graph.neighbors(node_id):
                visit(neighbor.id)

        visit(start)

        return order
