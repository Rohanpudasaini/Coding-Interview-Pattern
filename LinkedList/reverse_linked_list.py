from LinkedList import ListNode, build_list, to_list, cases

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

# Time complexity is O(N) as we are traversing the linked list once only
# Space complexity is O(N) because each recursion call is stored in stack and will use N space in stack
# caveat: This recursion call will fail in python if we tried linedlist with length more than 1000 as it will cause `RecursionError: maximum recursion depth exceeded`



print("Using Recursion")
for name, values in cases.items():
    head = build_list(values)
    result = to_list(reverse_linked_list_recursive(head))
    expected = values[::-1]
    status = "OK" if result == expected else "FAIL"
    print(f"{status:4} {name:14} {values=} ->  {result} (expected {expected})")


# print("Testing recursion with longer linked list")

# head = build_list(list(range(50000)))

# reverse_linked_list_recursive(head,None)