# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head

        while curr:
            curr = curr.next
            n += 1

        if not head or not head.next:
            return head

        k = k % n

        if k == 0:
            return head

        c = n - k
        curr = head
        leftPrev = None
        while c > 0:
            leftPrev = curr
            curr = curr.next
            c -= 1

        leftPrev.next = None

        newHead = curr
        while curr.next:
            curr = curr.next

        curr.next = head
        head = newHead
        return newHead


# @leet end

