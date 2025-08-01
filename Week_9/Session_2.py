
# Problem #2: Merge two sorted linked lists
# Given the heads of two sorted linked lists,
#  merge them into one sorted list by reusing nodes.
# Input: list1 = [2, 5, 7], list2 = [1, 3, 6]
# Output: [1, 2, 3, 5, 6, 7]
# Return the head of the merged list.


# linked lists are SORTED
# merge lists and have the final list be sorted

# will need a new linked list to hold the result
# if statement to check if either of the lists is empty if so then just reaturn the non-empty list

# Step 1: create a Node class
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Step 2: make a function to sort the nodes
# takes in 2 lists as parameters
def mergeSorted(list1, list2):
    # pointer for head of list 1
    ptr_1 = list1
    # pointer for head of list 2
    ptr_2 = list2

    
    
    if not list1:
        return list2
    else:
        return list1
    
    if ptr_1.val < ptr_2.val:
        new_list = 
    

