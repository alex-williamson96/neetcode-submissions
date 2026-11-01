# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = None
        while head != None:
            curr = head.next
            tmp = ListNode(head.val, tmp)            
            head = curr
        return tmp
