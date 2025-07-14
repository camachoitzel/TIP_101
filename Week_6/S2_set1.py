# Problem 1: Detect Circular Linked List
# A circular linked list is a linked list where the tail node points at the head node. 
# Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.
# Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.
# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(head):
#     current = head
#     while current.next:
#         current = current.next

#         if current.next == head:
#             return True
#     return False
     
    

# num1 = Node(1)
# num2 = Node(2)
# num3 = Node(3)
# num1.next = num2
# num2.next = num3
# num3.next = num1

# # num1 -> num2 -> num3 -> num1
# print(is_circular(num1))

# var1 = Node(1)
# var2 = Node(2)
# var3 = Node(3)
# var1.next = var2
# var2.next = var3
# var3.next = var1
# var1 = Node('var1', Node('var2', Node('var3')))
# # var1 -> var2 -> var3
# print(is_circular(var1))

# Problem 2: Find Last Node in a Linked List Cycle
# Given the head of a singly linked list, write a function that returns the last node in the cycle. 
# If there is no cycle in the linked list, return None.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_last_node_in_cycle(head):
     current = head
     seen = set()
     prev = None

     while current.next:
         if current not in seen:
             seen.add(current)
         else:
             return prev.value
         prev = current
         current = current.next


num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

print(find_last_node_in_cycle(num1))
