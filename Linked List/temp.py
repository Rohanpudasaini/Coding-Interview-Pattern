class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode| None)-> ListNode| None:
    curr_node : ListNode | None = head
    previous_node: ListNode | None = None
    
    while curr_node is not  None:
        next_node = curr_node.next
        curr_node.next = previous_node
        previous_node = curr_node
        curr_node = next_node
    return previous_node