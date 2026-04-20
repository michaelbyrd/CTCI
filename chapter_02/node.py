# Shared Node class for Chapter 2 — Linked Lists


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def to_list(node):
    """Convert linked list to Python list for easy comparison."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def from_list(values):
    """Build a linked list from a Python list. Returns head node."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head
