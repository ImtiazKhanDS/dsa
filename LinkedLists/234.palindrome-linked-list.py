# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        def reverse(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def isIdentical(n1, n2):
            while n1 and n2:
                if n1.val != n2.val:
                    return False
                n1 = n1.next
                n2 = n2.next
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1, head2 = head, reverse(slow)
        slow.next = None
        return isIdentical(head1, head2)


# @leet end

