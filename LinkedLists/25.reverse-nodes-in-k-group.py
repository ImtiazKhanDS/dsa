# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Think recursive approach
        # just do the k reverse and send the recursive call with next k chunk

        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next

        if cnt < k:
            return head

        curr = head
        prev = None
        cnt = 0
        while curr and cnt < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            cnt += 1

        head.next = self.reverseKGroup(curr, k)
        return prev


# @leet end

