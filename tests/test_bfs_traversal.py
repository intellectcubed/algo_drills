import os
import importlib

ACTIVE_IMPL = os.getenv("ALGO_IMPL", "practice_shells")
if "ALGO_IMPL" not in os.environ:
    print("⚠️  ALGO_IMPL not set — defaulting to 'practice_shells'.")

print(f'Using implementation: {ACTIVE_IMPL}')
Node = importlib.import_module(f"{ACTIVE_IMPL}.graphs.node").Node
BFSTraversal = importlib.import_module(f"{ACTIVE_IMPL}.graphs.bfs_traversal").BFSTraversal


def build_sample_graph():
    a, b, c, d, e = [Node(x) for x in "ABCDE"]
    a.add_neighbor(b)
    a.add_neighbor(c)
    b.add_neighbor(d)
    c.add_neighbor(e)
    d.add_neighbor(a)  # cycle back to A
    return a, b, c, d, e


def test_bfs_basic():
    a, _, _, _, _ = build_sample_graph()
    traversal = BFSTraversal()
    order = traversal.bfs(a)
    assert order[0] == "A"
    assert set(order) == {"A", "B", "C", "D", "E"}
    # BFS should visit A, then B/C, then D/E
    assert order.index("B") < order.index("D")
    assert order.index("C") < order.index("E")


def test_bfs_empty_graph():
    traversal = BFSTraversal()
    assert traversal.bfs(None) == []


def test_bfs_single_node():
    a = Node("A")
    traversal = BFSTraversal()
    assert traversal.bfs(a) == ["A"]


def test_bfs_disconnected_nodes():
    a, b = Node("A"), Node("B")
    traversal = BFSTraversal()
    assert traversal.bfs(a) == ["A"]
    assert traversal.bfs(b) == ["B"]


def test_bfs_self_loop():
    a = Node("A")
    a.add_neighbor(a)
    traversal = BFSTraversal()
    assert traversal.bfs(a) == ["A"]
