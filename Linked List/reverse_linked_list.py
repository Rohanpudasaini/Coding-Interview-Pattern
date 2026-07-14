class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode| None)-> ListNode| None:
    curr_node : ListNode | None = head
    previous_node: ListNode | None = None
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = previous_node
        previous_node = curr_node
        curr_node = next_node

    return previous_node

# Time complexity of this code is O(N) as we are traversing the linked list once only
# Space complexity is O(1) as we are using only three variables to store the nodes
    

def reverse_linked_list_recursive(head:ListNode|None, previous_node=None):
    if head is None:
        return previous_node
    next_node = head.next
    head.next = previous_node
    return reverse_linked_list_recursive(next_node, head)

def build_list(values):
    """Turn a Python list into a linked list, return the head."""
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head

def to_list(head):
    """Turn a linked list back into a Python list for easy comparison."""
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


cases = {
    "empty":          [],                    # None in, None out
    "single":         [1],                   # one node reverses to itself
    "two":            [1, 2],                # smallest real reversal
    "odd_length":     [1, 2, 3, 4, 5],
    "even_length":    [1, 2, 3, 4, 5, 6],
    "duplicates":     [7, 7, 7],            # repeated values still reverse
    "with_negatives": [-1, 0, 3, -8],
}

print("Using Iteration")
for name, values in cases.items():
    head = build_list(values)
    result = to_list(reverse_linked_list(head))
    expected = values[::-1]
    status = "OK" if result == expected else "FAIL"
    print(f"{status:4} {name:14} {values=} => {result} (expected {expected})")

print("Using Recursion")
for name, values in cases.items():
    head = build_list(values)
    result = to_list(reverse_linked_list_recursive(head))
    expected = values[::-1]
    status = "OK" if result == expected else "FAIL"
    print(f"{status:4} {name:14} {values=} ->  {result} (expected {expected})")