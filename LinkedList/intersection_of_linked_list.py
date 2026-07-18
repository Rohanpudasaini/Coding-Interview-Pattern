from LinkedList import ListNode
def intersection_of_linked_list(head1:ListNode | None, head2:ListNode | None) -> ListNode | None:
    seen = set()
    while head1:
        seen.add(head1)
        head1 = head1.next
    
    while head2:
        if head2 in seen:
            return head2
        head2 = head2.next
    
    return None

# The time complexity of this code is O(M + N) where M and N are the length of the linked lists
# The space complexity of this code is O(M) where M is the length of the linked list
