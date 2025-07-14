# Unit Test
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# def mys_funct(head):
#     current = head
#     output = []

#     while current:
#         if current.value % 2 == 0:
#             output.append(current.value)
#         current = current.next

#     return output

# head = Node(1, Node(2 , Node (3, Node(4))))

# output = mys_funct(head)
# print(output)

# def find_nth_from_end(head, n):
#     current = head
#     length = 0

#     while current:
#         length += 1
#         current = current.next
    
#     if n > length or n <= 0:
#         return None
    
#     nth_elem = length - n
#     current = head
#     for elem in range(nth_elem):
#         current = current.next
    
#     return current.value

# 2 ptr approach:

# def find_nth_from_end(head, n):
#     fast = head
#     slow = head

#     for i in range(n):
#         if not fast:
#             return None
        
#         fast = fast.next
    
#     while fast:

#         fast = fast.next
#         slow = slow.next
    
#     return slow.value
        

    



# n = 2

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# output = find_nth_from_end(a, 5)
# print(output)

def shuffle(head):
    if not head or not head.next:
        return head
    
    temp = head.next
    current = head
    prev= None
    
    while current and current.next:
        first = current
        second = current.next
        
        first.next = second.next
        second.next = first
        
        if prev:
            prev.next = second
        else:
            temp = second
            
        prev = first
        current = first.next
    
    return temp.next


head = Node('a', Node('b', Node('c', Node('d'))))

