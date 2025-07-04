# Problem 1: Battle Pokemon

# write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

# If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

# Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".

# class Pokemon():
#     def  __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp # hit points
#         self.damage = damage # The amount of damage this pokemon does to its opponent every attack
        
#     def attack(self, opponent):
#         opponent.hp = opponent.hp - self.damage
#         if opponent.hp <= 0:
#             opponent.hp = 0
#             print(f"{opponent.name} fainted")
#         else:
#             print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

# pikachu = Pokemon("Pikachu", 35, 20)
# bulbasaur = Pokemon("Bulbasaur", 45, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)

# # Problem 2: Convert to Linked List

# # A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# # In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# # In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# # Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next



# lst = ["Jigglypuff", "Wigglytuff"]
# node_1 = Node(lst[0])
# node_2 = Node(lst[1])
# node_1.next = node_2
          

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)


# # Problem 3: Add First
# # Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

# # It should insert new_node as the new head of the linked_list. The function returns new_node.

# # Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
		
# def add_first(head, new_node):
# 	new_node.next = head

# lst = ["Jigglypuff", "Wigglytuff"]
# node_1 = Node(lst[0])
# node_2 = Node(lst[1])
# node_1.next = node_2
# # Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)



# print(node_1.value, "->", node_1.next.value)

# # Problem 4: Get Tail

# # Write a function get_tail() that takes in the head of a linked list as a parameter.

# # It should print out the value of the tail of the list.

# # If the list is empty (head is None), return None.
# # Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
            
# def get_tail(head):
#     current = head
#     while current.next != None:
#         current = current.next
#     return current.value

# num1 = Node("num1")
# num2 = Node("num2")
# num3 = Node("num3")

# num1.next = num2
# num2.next = num3

# head = num1
# tail = get_tail(num1)
# print(tail)

# Problem 5: Replace Node
# Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original and replacement as parameters.

# The function updates any node with value original to have value replacement.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
    current = head

    while current != None:
        if current.value == original:
            current.value = replacement
        current = current.next

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"

current = head
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next
