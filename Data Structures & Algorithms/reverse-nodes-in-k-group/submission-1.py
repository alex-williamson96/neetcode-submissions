# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int, force=False) -> Optional[ListNode]:
        tmp = None
        i = 0
        h = head
        while head:
            if i >= k:
                h.next = self.reverseKGroup(head, k)
                break
            i += 1
            curr = head.next
            head.next = tmp
            tmp = head
            head = curr
        if i < k and not force:
            return self.reverseKGroup(tmp, k, True)
        return tmp

        