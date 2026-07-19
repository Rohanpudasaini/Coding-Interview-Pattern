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

# Optimized
# Is there a way to remove the set we are sing as it's consuming extra space, is there a way to complete this in O(1) space complexity?

def intersection_of_linked_list_optimized(head1:ListNode|None, head2: ListNode|None) -> ListNode | None:
    ptr1, ptr2 = head1, head2    
    while ptr1 != ptr2:
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1
    return ptr1

# The time complexity of this code is O(M + N) where M and N are the length of the linked lists
# The space complexity of this code is o(1) as we aren't using any extra space