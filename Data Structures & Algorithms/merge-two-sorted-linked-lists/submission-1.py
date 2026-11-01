# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        tmp = tail = ListNode()
        while list1 != None and list2 != None:

            if list1 and (list1.val <= list2.val):
                tmp2 = list1.next
                list1.next = None
                tail.next = list1
                tail = tail.next
                list1 = tmp2
            elif list2 and (list2.val <= list1.val):
                tmp2 = list2.next
                list2.next = None
                tail.next = list2
                tail = tail.next
                list2 = tmp2
        if list1 and tail:
            tail.next = list1
        if list2 and tail:
            tail.next = list2
        return tmp.next


        
