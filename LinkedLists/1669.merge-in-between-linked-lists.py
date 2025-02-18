# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        l1_start, l1_end = list1, list1
        for _ in range(a - 1):
            l1_start = l1_start.next
        for _ in range(b):
            l1_end = l1_end.next
        l2_end = list2
        while l2_end.next:
            l2_end = l2_end.next
        l1_start.next = list2
        l2_end.next = l1_end.next
        l1_end.next = None
        return list1


# @leet end

