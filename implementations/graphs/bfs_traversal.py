from collections import deque

class BFSTraversal:
    """Performs a breadth-first search on a graph given a starting node."""

    def bfs(self, start_node):
        if start_node is None:
            return []

        visited = set()
        order = []
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            order.append(node.name)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        return order
