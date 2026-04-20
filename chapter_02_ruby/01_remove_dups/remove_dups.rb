# Chapter 2 | Linked Lists
# Problem 2.1 — Remove Dups
#
# Write code to remove duplicates from an unsorted linked list.
# Follow up: how would you solve this if a temporary buffer is not allowed?
#
# Example:
#   Input:  1 -> 2 -> 3 -> 2 -> 1
#   Output: 1 -> 2 -> 3

require_relative '../node'
require 'set'

# Time: O(n), Space: O(n)
def remove_dups(head)
  seen = Set.new
  current, prev = head, nil

  while current do
    if seen.include?(current.val)
      prev.next = current.next
    else
      seen.add(current.val)
      prev = current
    end
     current = current.next
  end

  return head

end

# Time: O(n²), Space: O(1)
def remove_dups_no_buffer(head)
end
