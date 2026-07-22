class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def mid_point_of_linked_list(head:ListNode) -> ListNode:
    
    fast: ListNode = head
    slow: ListNode = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# Time complexity is O(N) as we are traversing the linkedlist only once
# Space complexity is O(1) as we arn't using any extra space

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    print(mid_point_of_linked_list(head).value)