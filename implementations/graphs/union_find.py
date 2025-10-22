class DisjointSet:
    """
    Union-Find (Disjoint Set Union) data structure with path compression
    and union by rank.
    """

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        print('*'*20)
        print(f'Finding root of {x}, current parent: {self.parent[x]}')
        """Find representative of set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union the sets that contain x and y."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # already connected

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    ds = DisjointSet(3)
    print(f'ds.union(0, 1): {ds.union(0, 1)}')
    print(f'ds.union(1, 2): {ds.union(1, 2)}')
    ds.union(2, 3)
    assert ds.connected(1, 3) == True
    assert ds.connected(1, 4) == False
    ds.union(4, 5)
    ds.union(5, 6)
    ds.union(3, 6)
    assert ds.connected(1, 6) == True
    print("All tests passed.")


    # Simple test cases
    # ds = DisjointSet(10)
    # print(f'ds.union(0, 1): {ds.union(0, 1)}')
    # print(f'ds.union(1, 2): {ds.union(1, 2)}')
    # ds.union(2, 3)
    # assert ds.connected(1, 3) == True
    # assert ds.connected(1, 4) == False
    # ds.union(4, 5)
    # ds.union(5, 6)
    # ds.union(3, 6)
    # assert ds.connected(1, 6) == True
    # print("All tests passed.")