import os
import importlib
import pytest

ACTIVE_IMPL = os.getenv("ALGO_IMPL", "practice_shells")
if "ALGO_IMPL" not in os.environ:
    print("⚠️  ALGO_IMPL not set — defaulting to 'practice_shells'.")

node_module = importlib.import_module(f"{ACTIVE_IMPL}.graphs.node")
dfs_module = importlib.import_module(f"{ACTIVE_IMPL}.graphs.dfs_traversal")

Node = node_module.Node
DFSTraversal = dfs_module.DFSTraversal


def test_basic_dfs():
    A, B, C, D = Node('A'), Node('B'), Node('C'), Node('D')
    A.add_neighbor(B)
    A.add_neighbor(C)
    B.add_neighbor(D)

    dfs = DFSTraversal()
    result = dfs.traverse(A)
    assert result == ['A', 'B', 'D', 'C']


def test_single_node():
    A = Node('A')
    dfs = DFSTraversal()
    assert dfs.traverse(A) == ['A']


def test_disconnected_graph():
    A, B, C, D = Node('A'), Node('B'), Node('C'), Node('D')
    A.add_neighbor(B)
    C.add_neighbor(D)

    dfs = DFSTraversal()
    result = dfs.traverse(A)
    assert result == ['A', 'B']


def test_cycle():
    A, B, C = Node('A'), Node('B'), Node('C')
    A.add_neighbor(B)
    B.add_neighbor(C)
    C.add_neighbor(A)

    dfs = DFSTraversal()
    result = dfs.traverse(A)
    assert result == ['A', 'B', 'C']


def test_none_start():
    dfs = DFSTraversal()
    assert dfs.traverse(None) == []


def test_large_graph_performance():
    # Build a long chain of 2000 nodes
    nodes = [Node(str(i)) for i in range(2000)]
    for i in range(1999):
        nodes[i].add_neighbor(nodes[i + 1])

    dfs = DFSTraversal()
    result = dfs.traverse(nodes[0])

    assert result[0] == '0'
    assert result[-1] == '1999'
    assert len(result) == 2000
