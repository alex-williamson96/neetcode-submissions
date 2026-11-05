# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l2 = lists[i + 1] if i < len(lists) - 1 else None
                merged.append(merge(lists[i], l2))
            lists = merged
        return lists[0]

def merge(l1, l2):
    head = ListNode()
    curr = head
    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
                tmp.next = None
                curr.next = tmp
            else:
                tmp = l2
                l2 = l2.next
                tmp.next = None
                curr.next = tmp
        elif l1:
            curr.next = l1
            return head.next
        elif l2:
            curr.next = l2
            return head.next
        curr = curr.next
    return head.next
