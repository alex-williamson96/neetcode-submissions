"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = dict()
        i_nodes = dict()
        i = 0
        tmp = head
        while tmp:
            nodes[tmp] = i
            tmp = tmp.next
            i += 1
        i = 0
        tmp = head
        while tmp:
            random = None
            if tmp.random:
                random = nodes[tmp.random]
            i_nodes[i] = (tmp.val, random) # value of each node and index it points to
            tmp = tmp.next
            i += 1

        copy = dict()
        dummy = Node(0)
        curr = dummy
        for n in range(i):
            curr.next = Node(i_nodes[n][0])
            copy[n] = curr.next
            curr = curr.next
        curr = dummy.next
        for n in range(i):
            if i_nodes[n][1] is not None:
                curr.random = copy[i_nodes[n][1]]
            curr = curr.next
        return dummy.next


