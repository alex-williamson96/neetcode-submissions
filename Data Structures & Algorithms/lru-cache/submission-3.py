class ListNode:
    def __init__(self, val, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
    
def remove(node):
    node.prev.next = node.next
    node.next.prev = node.prev

def insert_next(head, node):
    next = head.next
    head.next = node
    next.prev = node
    node.next = next
    node.prev = head
    return node


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        remove(node)
        insert_next(self.head, node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            self.cache.pop(self.tail.prev.key)
            remove(self.tail.prev)
        

        self.cache[key] = insert_next(self.head, ListNode(value, key=key))
        
