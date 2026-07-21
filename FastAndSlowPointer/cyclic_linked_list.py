class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def check_cyclic_link_list(head:ListNode)-> bool:
    visited = set()
    pointer = head
    while pointer:
        if pointer in visited:
            return True
        visited.add(pointer)
        pointer = pointer.next
    return False

# Bruteforce approach
# Time complexity: O(N) where n is the length of the linkedlist
# Space complexity is also O(N) as we are strong each node in a set

# Optimized: We can optimize this code to have space complexity of O(1).

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(check_cyclic_link_list(head))
