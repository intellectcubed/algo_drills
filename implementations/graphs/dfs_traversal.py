from .node import Node


class DFSTraversal:
    """
    Perform a Depth-First Search traversal on a graph of Node objects.

    Example:
        A = Node('A')
        B = Node('B')
        C = Node('C')
        A.add_neighbor(B)
        A.add_neighbor(C)
        dfs = DFSTraversal()
        order = dfs.traverse(A)
        print(order)  # ['A', 'B', 'C']
    """

    def __init__(self):
        self.visited = set()
        self.result = []

    def traverse(self, start_node: Node):
        """Iteratively traverse the graph from the given start node."""
        if not start_node:
            return []

        self.visited.clear()
        self.result.clear()
        stack = [start_node]

        # while stack:
        #     node = stack.pop()
        #     if node not in self.visited:
        #         self.visited.add(node)
        #         self.result.append(node.name)
        #         # Reverse to maintain left-to-right neighbor visit order
        #         for neighbor in reversed(node.neighbors):
        #             if neighbor not in self.visited:
        #                 stack.append(neighbor)

        while stack:
            node = stack.pop()
            self.visited.add(node)
            self.result.append(node.name)
            # Reverse to maintain left-to-right neighbor visit order
            for neighbor in reversed(node.neighbors):
                if neighbor not in self.visited:
                    stack.append(neighbor)

        return self.result
