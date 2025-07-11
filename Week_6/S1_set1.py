# Problem 1: Nested Constructors
# Step 1: Copy the following code into Replit.

# Step 2: Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 in a single assignment statement.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
# lst = Node(4, Node(3, Node(2)))

# Problem 2: Find Frequency
# Given the head of a linked list and a value val, return the frequency of val in the list. 
# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next


# def count_element(head, val):
# 	count = 0
# 	c = head
# 	while c:
# 		if c.value == val:
# 			count += 1
# 		c = c.next
# 	return count

# h = Node(3, Node(1, Node(2, Node(1))))
# i = count_element(h, 1)
# print(i)

# Problem 3: Remove Tail
# The following code attempts to remove the tail of a singly linked list. However, it has a bug!

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and 
# fix the bug so that the function correctly removes the tail of the list.

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
        
        
# # Helper function to print the linked list
# def print_list(node):
#     current = node
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()


# # I have a bug! 
# def remove_tail(head):
#     if head is None: # If the list is empty, return None
#         return None
#     if head.next is None: # If there's only one node, removing it leaves the list empty
#         return None 
		
# 	# Start from the head and find the second-to-last node
#     current = head
#     while current.next.next: 
#         current = current.next

#     current.next = None # Remove the last node by setting second-to-last node to None
#     return head

# h = Node(1, Node(2, Node(3, Node(4))))

# remove_tail(h)
# print_list(h)

# Problem 4: Find the Middle
# A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. 
# Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. 
# If there are two middle nodes, return the second middle node.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#        self.value = value
#        self.next = next
       
#     def print_list(node):
#         current = node
#         while current:
#             print(current.value, end=" -> " if current.next else "")
#             current = current.next
#         print()

# def find_middle_element(head):
#     slow = head 
#     fast = head

#     # find the middle
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow.value

# h = Node(1, Node(2, Node(3)))
# print(find_middle_element(h))

# Problem 5: Is Palindrome?
# Given the head of a singly linked list, return True if the values of the linked list are palindromic and False otherwise. 
# Use the two-pointer technique in your solution.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#        self.value = value
#        self.next = next



# def is_palindrome(head):
#     slow = head 
#     fast = head

#     # find the middle
#     while fast and fast.next:
#         slow = slow .next
#         fast = fast.next.next
    
#     # reverse the second half
#     prev = None
#     curr = slow

#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node

#     # compare 1st half and reversed 2nd half
#     first_half = head
#     second_half = prev

#     while second_half:
#         if first_half.value != second_half.value:
#             return False
#         first_half = first_half.next
#         second_half = second_half.next
    
#     return True


# h = Node(1, Node(2, Node(1)))
# print(is_palindrome(h))


# Problem 6: Put it in Reverse
# Given the head of a singly linked list, reverse the list, and return the reversed list. 
# You must reverse the list in place. Return the head of the reversed list.
# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def reverse(head):
    curr = head
    prev = None
    temp = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

h = Node(1, Node(2, Node(3, Node(4))))
new_head = reverse(h)
print(new_head.value)
print_list(new_head)

