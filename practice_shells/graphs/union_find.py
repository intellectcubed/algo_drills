class DisjointSet:
    """
    TODO: Implement a Union-Find (Disjoint Set Union) data structure
    with path compression and union by rank.
    """

    def __init__(self, n: int):
        # TODO: Initialize parent and rank arrays
        pass

    def find(self, x:int) -> int:
        """
        TODO: Implement find with path compression.
        Returns the representative of the set containing x.
        """
        pass

    def union(self, x: int, y: int) -> bool:
        """
        TODO: Implement union by rank.
        Merges the sets containing x and y.
        Return: 
            True if unioned
            False if already unioned
        """
        pass

    def connected(self, x:int, y:int) -> bool:
        """
        TODO: Return True if x and y belong to the same set.
        """
        pass

