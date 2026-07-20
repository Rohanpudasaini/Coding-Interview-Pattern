class ListNode:
    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.head = ListNode(0,None,None)
        self.tail = ListNode(0,None,None)
        self.cache = {}

    
    def get(self,key:int):
        pass
    
    def put(self, key:int, value:int):
        pass
    
    def remove_node(self, node:ListNode):
        pass
    
    def add_node(self, node:ListNode):
        pass
    

    