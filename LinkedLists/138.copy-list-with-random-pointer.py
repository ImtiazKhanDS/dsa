# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        curr = head
        mp = {}
        prev = None
        cloneHead = None
        # store the mappings from existing node to cloned node in a map
        while curr:
            tmp = Node(curr.val)
            mp[curr] = tmp
            if not prev:
                cloneHead = tmp
                prev = tmp
            else:
                prev.next = tmp
                prev = tmp
            curr = curr.next

        curr1 = head
        curr2 = cloneHead
        while curr2:
            curr2.random = mp.get(curr1.random)
            curr2 = curr2.next
            curr1 = curr1.next
        return cloneHead


# @leet end

