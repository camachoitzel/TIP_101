# Problem 1: Detect Circular Linked List
# A circular linked list is a linked list where the tail node points at the head node. 
# Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.
# Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.
# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    current = head
    while current.next:
        current = current.next

        if current.next == head:
            return True
    return False
     
    

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1

# num1 -> num2 -> num3 -> num1
print(is_circular(num1))

var1 = Node('var1', Node('var2', Node('var3')))
# var1 -> var2 -> var3
print(is_circular(var1))