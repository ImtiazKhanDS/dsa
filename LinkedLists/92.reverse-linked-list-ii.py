# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head and not head.next:
            return head

        dum = ListNode(0, head)
        leftprev, curr = dum, head
        for _ in range(left - 1):
            leftprev, curr = curr, curr.next

        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            curr, prev = temp, curr

        leftprev.next.next = curr
        leftprev.next = prev
        return dum.next


# @leet end

