from LinkedList import ListNode, build_list, to_list, cases



def delete_nth_last_node(head:ListNode|None, n:int) -> ListNode|None:
    dummy: ListNode | None = ListNode(0, head)
    front: ListNode | None = dummy
    back: ListNode | None = dummy
    for _ in range(n+1):
        front: ListNode | None = front.next

    if front is None:
        return dummy.next
    while front.next:
        front = front.next
        back = back.next
    back.next = back.next.next

    return dummy.next


print("Using Iteration")
for name, values in cases.items():
    head = build_list(values)
    result = to_list(delete_nth_last_node(head, 2))
    expected = values[1:]
    status = "OK" if result == expected else "FAIL"
    print(f"{status:4} {name:14} {values=} => {result} (expected {expected})")