import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import from_list, to_list
from delete_middle_node import delete_middle_node


def get_node(head, index):
    """Return the node at the given index."""
    for _ in range(index):
        head = head.next
    return head


@pytest.mark.parametrize("fn", [delete_middle_node])
class TestShortInput:
    def test_delete_middle_of_three(self, fn):
        head = from_list([1, 2, 3])
        fn(get_node(head, 1))
        assert to_list(head) == [1, 3]

    def test_delete_second_of_five(self, fn):
        head = from_list([1, 2, 3, 4, 5])
        fn(get_node(head, 1))
        assert to_list(head) == [1, 3, 4, 5]

    def test_delete_third_of_five(self, fn):
        head = from_list([1, 2, 3, 4, 5])
        fn(get_node(head, 2))
        assert to_list(head) == [1, 2, 4, 5]

    def test_delete_fourth_of_five(self, fn):
        head = from_list([1, 2, 3, 4, 5])
        fn(get_node(head, 3))
        assert to_list(head) == [1, 2, 3, 5]

    def test_delete_middle_of_letters(self, fn):
        head = from_list(['a', 'b', 'c', 'd', 'e'])
        fn(get_node(head, 2))
        assert to_list(head) == ['a', 'b', 'd', 'e']


@pytest.mark.parametrize("fn", [delete_middle_node])
class TestMediumInput:
    def test_delete_middle_of_50(self, fn):
        vals = list(range(50))
        head = from_list(vals)
        fn(get_node(head, 25))
        expected = vals[:25] + vals[26:]
        assert to_list(head) == expected

    def test_delete_near_end_of_50(self, fn):
        vals = list(range(50))
        head = from_list(vals)
        fn(get_node(head, 48))
        expected = vals[:48] + vals[49:]
        assert to_list(head) == expected


@pytest.mark.slow
@pytest.mark.parametrize("fn", [delete_middle_node])
class TestLongInput:
    def test_delete_middle_of_1000(self, fn):
        vals = list(range(1000))
        head = from_list(vals)
        fn(get_node(head, 500))
        expected = vals[:500] + vals[501:]
        assert to_list(head) == expected
