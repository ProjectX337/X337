from __future__ import annotations

from collections import deque

from .graph import Graph
from .node import GraphNode


class GraphTraversal:
    """
    Basic graph traversal utilities.

    Future planners and agents should use this
    instead of manually walking relationships.
    """

    def __init__(self, graph: Graph):

        self.graph = graph

    # ---------------------------------------------------------

    def bfs(
        self,
        start: str,
    ) -> list[GraphNode]:

        visited = set()

        queue = deque([start])

        order: list[GraphNode] = []

        while queue:

            node_id = queue.popleft()

            if node_id in visited:
                continue

            visited.add(node_id)

            if self.graph.has_node(node_id):

                node = self.graph.get(node_id)

                order.append(node)

                for neighbor in self.graph.neighbors(node_id):

                    if neighbor.id not in visited:

                        queue.append(neighbor.id)

        return order

    # ---------------------------------------------------------

    def dfs(
        self,
        start: str,
    ) -> list[GraphNode]:

        visited = set()

        order: list[GraphNode] = []

        def visit(node_id: str):

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
