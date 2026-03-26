# Chapter 2 | Linked Lists
# Problem 2.1 — Remove Dups
#
# Write code to remove duplicates from an unsorted linked list.
# Follow up: how would you solve this if a temporary buffer is not allowed?
#
# Example:
#   Input:  1 -> 2 -> 3 -> 2 -> 1
#   Output: 1 -> 2 -> 3
#
# Benchmarks (avg over 100 runs):
#   n=10      remove_dups=0.0018ms  remove_dups_no_buffer=0.0024ms
#   n=100     remove_dups=0.0153ms  remove_dups_no_buffer=0.1115ms
#   n=1000    remove_dups=0.1365ms  remove_dups_no_buffer=2.2224ms
#   n=10000   remove_dups=1.3261ms  remove_dups_no_buffer=20.3098ms
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from node import Node, to_list, from_list


# Time: O(n), Space: O(n)
def remove_dups(head):
    seen = set()
    current, prev = head, None

    while current:
        if current.val in seen:
            prev.next = current.next
        else:
            seen.add(current.val)
            prev = current
        current = current.next
    return head


# Time: O(n²), Space: O(1)
def remove_dups_no_buffer(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head
