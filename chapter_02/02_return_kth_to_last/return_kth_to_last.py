# Chapter 2 | Linked Lists
# Problem 2.2 — Return Kth to Last
#
# Implement an algorithm to find the kth to last element of a singly linked list.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5, k=2
#   Output: 4  (2nd to last)
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from node import Node, to_list, from_list


def return_kth_to_last_two_pass(head, k):
    counter = 0
    current = head
    while current:



def return_kth_to_last_two_pointers(head, k):
    pass
