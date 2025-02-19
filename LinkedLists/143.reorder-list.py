# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Splitting the list into two halves.
        # 2. Reversing the second half.
        # 3. Merging the two halves in an alternating fashion.
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head1, head2 = head, prev

        while head1 and head2:
            temp = head1.next
            head1.next = head2
            head1 = temp
            temp2 = head2.next
            head2.next = temp
            head2 = temp2


# @leet end

