# Chapter 2 | Linked Lists
# Problem 2.2 — Return Kth to Last
#
# Implement an algorithm to find the kth to last element of a singly linked list.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5, k=2
#   Output: 4  (2nd to last)

require_relative '../node'

# Approach: two-pass (count length, then traverse)
# Time: O(n), Space: O(1)
def return_kth_to_last_two_pass(head, k)
  distance = list_length(head) - k 
  out = head
  distance.times do 
    out = out.next
  end
  out.val

end

# Approach: two pointers
# Time: O(n), Space: O(1)
def return_kth_to_last_two_pointers(head, k)
  leader = head
  follower = head

  k.times do 
    leader = leader.next
  end

  until leader.nil?
    leader = leader.next
    follower = follower.next
  end

  follower.val
end

# Benchmark results (1,000 runs, k = size / 2):
#
#                  n=100    n=1,000   n=10,000
# two_pass         0.0044s  0.0418s   0.4197s
# two_pointers     0.0036s  0.0328s   0.3292s   <- ~20% faster (single pass)
#
# Complexity:
#
#     | approach      | time  | space |
#     |---------------|-------|-------|
#     | two_pass      | O(n)  | O(1)  |
#     | two_pointers  | O(n)  | O(1)  |
#
#     Both are O(n) time and O(1) space. two_pointers is faster in practice
#     because it makes one pass vs two.
