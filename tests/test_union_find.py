import importlib
import os

ACTIVE_IMPLEMENTATION = os.getenv("ALGO_IMPL", "practice_shells")
if "ALGO_IMPL" not in os.environ:
    print("⚠️  ALGO_IMPL not set — defaulting to 'practice_shells'.")

DisjointSet = importlib.import_module(f"{ACTIVE_IMPLEMENTATION}.graphs.union_find").DisjointSet

def test_union_find_basic():
    ds = DisjointSet(5)
    # Initially, all elements are disconnected
    for i in range(5):
        assert ds.find(i) == i

    # Union some sets
    ds.union(0, 1)
    ds.union(1, 2)

    assert ds.connected(0, 1)
    assert ds.connected(1, 2)
    assert ds.connected(0, 2)
    assert not ds.connected(0, 3)

def test_union_find_redundant_union():
    ds = DisjointSet(3)
    # print(f'Value returned: {ds.union(0, 1)}')
    assert ds.union(0, 1)
    # Redundant union should return False
    assert not ds.union(0, 1)
    assert ds.connected(0, 1)

def test_union_find_path_compression():
    ds = DisjointSet(6)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(2, 3)
    root_before = ds.find(0)
    ds.find(3)
    # After compression, all should have same root
    for i in range(4):
        assert ds.find(i) == root_before

