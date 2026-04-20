import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import Node
from loop_detection import loop_detection


def make_loop(before_loop, loop_vals, loop_start_index=0):
    """Build a linked list with a loop.
    before_loop: values before the loop starts
    loop_vals: values in the loop
    loop_start_index: index within loop_vals where the tail reconnects
    Returns (head, loop_start_node)
    """
    nodes = [Node(v) for v in before_loop + loop_vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    loop_start = nodes[len(before_loop) + loop_start_index]
    nodes[-1].next = loop_start
    return nodes[0], loop_start


@pytest.mark.parametrize("fn", [loop_detection])
class TestShortInput:
    def test_loop_at_start(self, fn):
        head, loop_start = make_loop([], [1, 2, 3, 4, 5])
        assert fn(head) is loop_start

    def test_loop_after_prefix(self, fn):
        head, loop_start = make_loop([1, 2], [3, 4, 5])
        assert fn(head) is loop_start

    def test_loop_of_one(self, fn):
        node = Node(1)
        node.next = node
        assert fn(node) is node

    def test_single_loop_with_prefix(self, fn):
        head, loop_start = make_loop([1, 2, 3], [4])
        assert fn(head) is loop_start

    def test_no_loop(self, fn):
        node = Node(1)
        node.next = Node(2)
        node.next.next = Node(3)
        assert fn(node) is None


@pytest.mark.parametrize("fn", [loop_detection])
class TestMediumInput:
    def test_long_prefix_short_loop(self, fn):
        head, loop_start = make_loop(list(range(50)), list(range(50, 60)))
        assert fn(head) is loop_start

    def test_short_prefix_long_loop(self, fn):
        head, loop_start = make_loop(list(range(5)), list(range(5, 55)))
        assert fn(head) is loop_start


@pytest.mark.slow
@pytest.mark.parametrize("fn", [loop_detection])
class TestLongInput:
    def test_1000_nodes_with_loop(self, fn):
        head, loop_start = make_loop(list(range(500)), list(range(500, 1000)))
        assert fn(head) is loop_start

    def test_no_loop_1000_nodes(self, fn):
        nodes = [Node(i) for i in range(1000)]
        for i in range(999):
            nodes[i].next = nodes[i + 1]
        assert fn(nodes[0]) is None
