# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while slow:
            i = n
            while i > 0:
                fast = fast.next
                i -= 1
            if not fast:
                break
            slow = slow.next
            fast = slow
        
        curr = head
        prev = None
        while curr:
            if curr is slow:
                if prev:
                    prev.next = curr.next
                    return head
                else:
                    return curr.next
            i += 1
            prev = curr
            curr = curr.next
        return head
        