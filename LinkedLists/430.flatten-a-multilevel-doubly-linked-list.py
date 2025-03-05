# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        def flatten_dfs(node):
            curr = node
            last = None
            while curr:
                if curr.child:
                    child = curr.child
                    curr.child = None
                    next_node = curr.next
                    curr.next = child
                    child.prev = curr
                    last = flatten_dfs(child)
                    if next_node:
                        last.next = next_node
                        next_node.prev = last
                last = curr
                curr = curr.next
            return last

        flatten_dfs(head)
        return head


# @leet end

