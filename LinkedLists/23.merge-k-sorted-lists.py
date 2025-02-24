# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def MergeRecursive(self, h1: ListNode, h2: ListNode):
        if not h1:
            return h2
        if not h2:
            return h1

        head = None
        temp = None
        if h1.val <= h2.val:
            head = h1
            temp = head.next
            head.next = None
            head.next = self.MergeRecursive(temp, h2)
        else:
            head = h2
            temp = head.next
            head.next = None
            head.next = self.MergeRecursive(h1, temp)

        return head

    def MergeK(self, listHeads: List, i: int, j: int):
        if i == j:
            return listHeads[i]
        m = (i + j) // 2
        h1 = self.MergeK(listHeads, i, m)
        h2 = self.MergeK(listHeads, m + 1, j)
        return self.MergeRecursive(h1, h2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return None
        return self.MergeK(lists, 0, len(lists) - 1)


# @leet end

