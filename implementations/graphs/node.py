class Node:
    """A simple graph node with a name and list of neighbors."""

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def __repr__(self):
        return f"Node({self.name})"
