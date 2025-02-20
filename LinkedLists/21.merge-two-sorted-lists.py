# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newHead = ListNode(0, None)
        finalHead = newHead
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                newHead.next = l1
                l1 = l1.next
            else:
                newHead.next = l2
                l2 = l2.next

            newHead = newHead.next

        if l1:
            newHead.next = l1

        if l2:
            newHead.next = l2

        return finalHead.next


# @leet end

