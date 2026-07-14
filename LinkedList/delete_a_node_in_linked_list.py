from LinkedList import ListNode, build_list, to_list, cases

# My solution
# def delete_a_node_in_linkd_list(head:ListNode|None, value:int) -> ListNode | None:
#     if head is None:
#         return None
#     if head.val == value:
#         return head.next
#     previous_node: ListNode | None = None
#     curr_node : ListNode | None = head
#     while curr_node is not None:
#         if curr_node.val == value:
#             previous_node.next = curr_node.next
#             return head
#         previous_node = curr_node
#         curr_node = curr_node.next
#     return head


# Claude's solution
def delete_a_node_in_linkd_list(head:ListNode|None, value:int) -> ListNode| None:
    dummy_node = ListNode(0,head)
    previous_node, current_node = dummy_node, head
    while current_node is not None:
        if current_node.val == value:
            previous_node.next = current_node.next
            return dummy_node.next
        previous_node = current_node
        current_node = current_node.next
    return head


print("Using Iteration")
for name, values in cases.items():
    head = build_list(values)
    result = to_list(delete_a_node_in_linkd_list(head, values[0] if values else -2000))
    expected = values[1:]
    status = "OK" if result == expected else "FAIL"
    print(f"{status:4} {name:14} {values=} => {result} (expected {expected})")