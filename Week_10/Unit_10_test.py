# remove_head function

# class Node:
#     def __init__(self, val = 0, prev = None, next = None):
#         self.val = val
#         self.prev = prev
#         self.next = next

# def remove_head(head):
#     if head is None:
#         return None
    
#     new_head = head.next
#     return new_head
    

# head = Node(1)
# head.next = Node(2)
# head.next.prev = Node(1)
# head.next.next = Node(3)
# head.next.next.prev = Node(2)

# print(remove_head(head).val)




# def longest_palindrome(s):
#     seen = {}
#     count = 0

#     for char in s:
#         if char in seen:
#             seen[char] += 1
#         else:
#             seen[char] = 1

#     odd = False

#     for value in seen.values():

#         count += (value // 2) * 2

#         if value % 2 == 1:

#             odd = True
    
#     if odd:
#         count += 1
    
#     return count

    

# s = "abccccdd"

# print(longest_palindrome(s))

# class Node:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next

# def has_cycle(head):
#     if not head:
#         return False
    
#     seen = set()
#     current = head

#     while current:
#         if current in seen:
#             return True
        
#         seen.add(current)
#         current = current.next
    
#     return False

    

def peak_element(nums):
    if not nums:
        return None
    
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo

# nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]

print(peak_element(nums))