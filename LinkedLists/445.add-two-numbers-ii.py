# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        num1 = ""
        num2 = ""
        while c1:
            num1 += str(c1.val)
            c1 = c1.next
        while c2:
            num2 += str(c2.val)
            c2 = c2.next

        num = eval(num1) + eval(num2)
        if num == 0:
            return ListNode(0)
        head = None
        prev = None
        while num:
            rem = num % 10
            num = num // 10
            temp = ListNode(rem)
            if not head:
                head = temp
                prev = temp
            else:
                head = temp
                head.next = prev
                prev = temp
        return head


# @leet end

