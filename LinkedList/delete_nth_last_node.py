from LinkedList import ListNode, build_list, to_list

# My implementation
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

# Claude Implementation
# def delete_nth_last_node(head: ListNode | None, n: int) -> ListNode | None:
#     dummy = ListNode(0, head)
#     front = dummy
#     back = dummy
#     for _ in range(n + 1):
#         front = front.next
#     while front:                      # was: while front.next
#         front = front.next
#         back = back.next
#     back.next = back.next.next        # front is None here; no guard needed
#     return dummy.next

cases = {
    # (values, n, expected)
    "middle":        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    "remove_last":   ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),   # tail
    "remove_head":   ([1, 2, 3],       3, [2, 3]),          # n == length
    "single":        ([1],             1, []),              # list becomes empty
    "two_del_first": ([1, 2],          2, [2]),
    "two_del_last":  ([1, 2],          1, [1]),
}

for name, (values, n, expected) in cases.items():
    result = to_list(delete_nth_last_node(build_list(values), n))
    status = "OK" if result == expected else "FAIL"
    print(f"{status:4} {name:14} n={n} -> {result} (expected {expected})")