# Unit 5

# class Node: 
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# def get_last(head):
#     if not head:
#         return None
    
#     current = head
#     while current:
#         current = current.next
#     return current.value

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# node1.next = node2
# node2.next = node3

# get_last(node1)

# class Person:
#     def __init__(self, first, last):
#         self.last_name = last
#         self.first_name = first
#         self.children = []
    
#     def add_child(self, child):
#         self.children.append(child)
    
#     def get_grandchildren(self):
#         grandchildren = []

#         for child in self.children:
#             for grandchild in child.children:
#                 grandchildren.append(grandchild)
        
#         return grandchildren



    
# johndoe = Person("John", "Doe")
# janedoe = Person("Jane", "Doe")
# jimmydoe = Person("Jimmy", "Doe")
# johndoe.add_child(janedoe)
# janedoe.add_child(jimmydoe)
# print(johndoe.get_grandchildren())

class Node: 
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

def extend_linked_list(tail,values):
    result = []
    current = tail



lst = '->'.join(['a', 'b', 'c'])
print(lst)
tail = 'c'
values = ['d', 'e', 'f']