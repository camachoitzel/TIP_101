# Instructor demo

# Multiple Pass
class Node: 
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

head = Node(2, Node(4 , Node (8, Node(1, Node (3)))))

# first pass: get the length
def get_length(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

# second pass: find the middle node
def find_middle(head):
    lenght = get_length(head)
    mid_index = lenght // 2
    curr = head
    for _ in range(mid_index):
        curr = curr.next
    return curr.value

print()

# temp head

def remove_duplicates(head):
    temp = Node(0)
    temp.next = head
    curr = head

    while curr and curr.next:
        if curr.value == curr.next.value:
            # skip the duplicate node
            curr.next = curr.next.next
        else:
            curr = curr.next
    return temp.next

# slow-fast technique

# create linked list: 1 -> 2 -> 2 -> 1
head = Node(2, Node(1 , Node (2, Node(2, Node (1)))))

def is_palindrome(head):
    slow = head 
    fast = head

    # find the middle
    while fast and fast.next:
        slow = slow .next
        fast = fast.next.next
    
    # reverse the second half
    prev = None
    curr = slow

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # compare 1st half and reversed 2nd half
    first_half = head
    second_half = prev

    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half.next
    
    return True