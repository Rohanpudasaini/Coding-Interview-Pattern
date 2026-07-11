# Linked Lists
Linked list is a datastructure consisting of sequence of nodes. Here each nodes will have mostly two componenets `value` and `next`

```
[Node1 | Addr1] -> [Node2 | Addr2] -> [Node3 | Addr3] -> NULL
```
The componenets can also have previous if the linked list is of `Doubly` type. In such a type there will be two pointers `prev` and `next`

## Use of Linked list
One of the best use of linked list is it's ability to increase and srink it's size. It can grow or shrink dynamically as per the requirement. unlike the array where we need to define the size of the array at the time of creation. Also, in linked list it is really easy to insert and delete a node. Unlike array where we need to shift the elements to the right or left to insert or delete a node. If we use array, then to insert or delete an element at index `i` we need to shift all the elements from index `i` to the end of the array. But in linked list, we just need to change the pointers of the nodes. For example lets say we need to delete a node at index `i`, then we need to change the pointer of the node at index `i-1` to point to the node at index `i+1`.


### Node Structure
```python
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
```

### Doubly Node Structure
```python
class DoublyNode:
    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
```
## Type of Linked Lists

1. Singly Linked List:
    This is a simple type of linked list and have two componenets and starts with a node called as Heads and will always ends with None. To access any elements in the linked list we need to traverse the whole data structure

2. Doubly Linked List:
    This is a slightly more complex type of linked list and have three componenets and starts with a node called as Heads and will always ends with None. It also have a pointer to the previous node. We can traverse the linked list in both forward and backward direction.


## Reverse Linked Lists
```Python
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head:ListNode) -> ListNode:
    current_node : ListNode | None = head
    previous_node : ListNode | None = None

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    
    return previous_node

```