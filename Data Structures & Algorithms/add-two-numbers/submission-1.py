# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode()
        curr = a
        remainder = 0
        while l1 or l2:
            total = remainder
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            remainder = total // 10
            # print('total: ', total)
            # print('total % 10: ', total % 10)
            # print('total // 10: ', total // 10)
            # print('remainder: ', remainder)
            # print()
            curr.next = ListNode(total % 10)
            curr = curr.next
        if remainder:
            curr.next = ListNode(remainder)
        return a.next