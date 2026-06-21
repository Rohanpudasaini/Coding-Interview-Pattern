# Two Pointers
 
 Pointers: Variable representing index or position within the data structure.
 Usually we used single pointer in normal case
 
```python
def print_list(my_data_structure):
    for i in range(len(my_data_structure)):
        print(my_data_structure[i])    
```
Here `i` is the single pointer

Now, let's add second pointer `j` to find sum of eact elements in the list with each other

```python
def sum_of_two_pointers(my_data_structure):
    for i in range(len(my_data_structure)):
        for j in range(len(my_data_structure)):
            print(f"{i} + {j} = {i+j}}")    
```
In the code above we used two pointers `i` and `j` to find the sum of each element with each other.

This is a brute force method and if we have single look across the code, we can see the time complexity as O(n^2)
That's really bad case, but we only want to intoduce second pointer.

Usually while using two pointer as we intended, the time complecity is usually dropped to O(n) by omiting the inner loop.

There are three type of two pointer approach.

1. Inward Traversal
Here both pointer start at opposite end of the data structure and would move towards each other.
This type of pointer is used when we want to do some operation by comparing two or more elements and switching them. 
Example of this:
```python
def reverse_list_inplace(data):
    left, right = 0, len(data) - 1
    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return data # We don't need to exclusivly reture data here as we are changing the data inplace that will update the original list. ()

    # TODO: Learn about python's peculiar nature of pass by object refrence.
    # TODO: To learn more about this what do you think would have happened if the data passed was say integer and we changed the integer inside the function. Would that have propagated outside of the function too??
    # TODO: Also what if the data passed was tuple and we tried to change the tuple(the whole tuple and not the elements as we can't exactly change the elements of tuple in python) inside the function. Would that have propagated outside of the function too??   
```

If you have spend a little time with Python you know we could easily reverse the list by simply doing `data[::-1]` but, that's python specific trick, in other languages you cannot do that. And also while doing `data[::-1]` time complexity is O(n) as it create a new list, copying all the elements in reverse order. So this is not a good way to reverse the list. So we need to use two pointers to reverse the list *inplace*.

2. Unidirectional Traversal
Here both pointer start at same end of the data structure and would move in same direction.
This type of pointer is used when we want to do some operation by comparing two or more elements and switching them. 
Example of this:
```python
def change_duplicate_elements_to_negative_in_sorted_array(data):
    left, right = 0, 1
    while right < len(data):
        if data[left] == data[right]:
            data[right] = -data[right]
        else:
            left = right
        right += 1
```

3. Staged Traversal
Here we use two pointers to traverse the data structure in two different stages. 
First pointer search and mark elements to be moved/changed and second pointer actually moves the element. It's like first loop identify and second loop do the task.
Example of this:
```Python
def move_all_zeros_to_end(data):
    i, j = 0, 0 # Using i as the first pointer and j as the second pointer
    while i < len(data):
        if data[i] != 0:
            data[i], data[j] = data[j], data[i] # Swapping the elements
            j += 1
        i += 1  
    return data
```


