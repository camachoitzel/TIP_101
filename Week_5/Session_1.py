# Instructor Demo

# custom class

class Student:
    # specify what attributes you want
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Hello")


nina_the_student = Student("Nina")

print(nina_the_student.name)

# Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(2)
b = Node(4)
# c= Node(6)

# a.next = b
# b = None
a.next = Node(4)
a.next.next =Node(6)

current = a
while current != None:
    print(current.value)
    current = current.next