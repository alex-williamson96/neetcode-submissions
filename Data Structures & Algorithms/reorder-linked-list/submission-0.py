# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        rev = slow.next
        slow.next = None
        
        
        tmp = None
        curr = rev
        while curr != None:
            curr = rev.next
            rev.next = tmp
            tmp = rev
            rev = curr
        rev = tmp
        

        curr = head
        while rev:
            temp = curr.next
            curr.next = rev
            rev = rev.next
            curr.next.next = temp
            curr = temp
