class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

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