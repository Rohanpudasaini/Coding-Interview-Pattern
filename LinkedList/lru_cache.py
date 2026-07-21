class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.cache = {}

    
    def get(self,key:int):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)
        return node.value
    
    def put(self, key:int, value:int):
        if key in self.cache:
            self.remove_node(self.cache[key])
            del self.cache[key]

        if len(self.cache) >= self.capacity:
            last_node = self.head.next
            self.remove_node(last_node)
            del self.cache[last_node.key]
        node_to_add = ListNode(key, value)
        self.add_node(node_to_add)
        self.cache[key] = node_to_add

    def remove_node(self, node:ListNode):
        prev_node = node.previous
        next_node = node.next
        prev_node.next = next_node
        next_node.previous = prev_node
    
    def add_node(self, node:ListNode):
        previous_node = self.tail.previous
        previous_node.next = node
        node.previous = previous_node
        node.next = self.tail
        self.tail.previous = node
    

# The time complexity of this code is
# For all functions: O(1) as we are only working on a simgle point and no traversal is needed

# The space complexity of this code is
# O(n) where n is capacity given as both the cache(hashmap) and linklist occupy space related to the capacity ~= n