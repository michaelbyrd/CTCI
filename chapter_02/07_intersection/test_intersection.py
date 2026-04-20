import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import Node, from_list
from intersection import intersection


def make_intersecting(a_vals, b_vals, shared_vals):
    """Build two lists that share a common tail by reference."""
    shared = from_list(shared_vals)
    # build list A ending at shared
    head_a = from_list(a_vals) if a_vals else None
    if head_a:
        node = head_a
        while node.next:
            node = node.next
        node.next = shared
    else:
        head_a = shared
    # build list B ending at shared
    head_b = from_list(b_vals) if b_vals else None
    if head_b:
        node = head_b
        while node.next:
            node = node.next
        node.next = shared
    else:
        head_b = shared
    return head_a, head_b, shared


@pytest.mark.parametrize("fn", [intersection])
class TestShortInput:
    def test_intersects(self, fn):
        a, b, shared = make_intersecting([1, 2, 3], [4, 5], [7, 8])
        assert fn(a, b) is shared

    def test_no_intersection(self, fn):
        a = from_list([1, 2, 3])
        b = from_list([4, 5, 6])
        assert fn(a, b) is None

    def test_same_list(self, fn):
        a = from_list([1, 2, 3])
        assert fn(a, a) is a

    def test_intersect_at_first_node(self, fn):
        shared = Node(1)
        assert fn(shared, shared) is shared

    def test_different_lengths_intersect(self, fn):
        a, b, shared = make_intersecting([1, 2, 3, 4], [5], [6, 7])
        assert fn(a, b) is shared

    def test_empty_lists(self, fn):
        assert fn(None, None) is None

    def test_one_empty(self, fn):
        a = from_list([1, 2, 3])
        assert fn(a, None) is None


@pytest.mark.parametrize("fn", [intersection])
class TestMediumInput:
    def test_long_lists_intersect(self, fn):
        a, b, shared = make_intersecting(list(range(25)), list(range(25, 50)), list(range(50, 75)))
        assert fn(a, b) is shared

    def test_long_lists_no_intersection(self, fn):
        a = from_list(list(range(50)))
        b = from_list(list(range(50, 100)))
        assert fn(a, b) is None


@pytest.mark.slow
@pytest.mark.parametrize("fn", [intersection])
class TestLongInput:
    def test_1000_nodes_intersect(self, fn):
        a, b, shared = make_intersecting(list(range(500)), list(range(500, 750)), list(range(750, 1000)))
        assert fn(a, b) is shared
