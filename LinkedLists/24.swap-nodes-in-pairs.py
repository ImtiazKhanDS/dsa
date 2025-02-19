# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        prev = None
        c = 0
        while c < 2:
            if prev:
                firstNode = prev
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
            c += 1

        firstNode.next = self.swapPairs(curr)
        return prev


# @leet end

