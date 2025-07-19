# Unit Test 7

# Given and alphabetically sorted list of strings names and string val
# return the index of the first occurence of val in O(log n) time

# Iterative

# def find_val(names, val):
#     index = 0

#     if val not in names:
#         return -1
    
#     for i in range(len(names)):
#         index = i
#         if val in names[i]:
#            return index
#         else:
#             i += 1
#     return index 

# recursive

def find_val(names, val):
    left = 0
    right = len(names) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if names[mid] == val:
            return mid
        elif names[mid] < val:
            left = mid + 1
            
        else:
            right = mid - 1
           
    return -1

# def bin_search(lst, target):
#     left = 0
#     right = len(lst) - 1
    
#     if left > right:
#         return - 1
    
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == val:
#             return mid
#         elif lst[mid] < val:
#             left = mid + 1
            
#         else:
#             right = mid - 1
           
#     return -1
    

names = ['Amal', 'Beric', 'Florin', 'Julie', 'Qin']
val = 'Julie'

result = find_val(names, val)
print(result)
print("\n")


# Example 1:
# Input: names = ['Amal', 'Beric', 'Florin', 'Julie', 'Qin'], val = 'Julie'
# Output: 3

# Example 2:
# Input: names = ['Amal', 'Beric', 'Florin', 'Julie', 'Qin'], val = 'Tabrez'
# Expected Output: -1


# Given two intergers x and n, where n >= 0, 
# write a function power() that recursively computes and returns x^n


def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

x = -3
n = 3

result = power(x, n)
print(result)
print("\n")

# Example 1:
# Input: x = 2, n = 3
# Output: 8

# Example:
# Input: x = 5, n = 0
# Output: 1

# Example 3:
# Input: x = -3, n = 3
# Output: -27


# Given a list of integers 'nums' sorted in non-decreasing order
# find the starting and ending position of a given target value. 
# return the result as a list in the form [start_pos, end_pos]
# if target not in list return [-1, -1]
# must be O(log n)

def search(nums, target):
    left = 0
    right = len(nums) - 1
    start_pos = -1

    # find start position
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] < target:
            left = mid + 1
        
        elif nums[mid] > target :
            right = mid - 1

        else:
            start_pos = mid
            # keep searching left
            right = mid -1
    
    left = 0
    right = len(nums) - 1
    end_pos = -1

    # find start position
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] < target:
            left = mid + 1
        
        elif nums[mid] > target :
            right = mid - 1

        else:
            end_pos = mid
            # keep searching right
            left = mid + 1
    
    return [start_pos , end_pos]
    

nums = [5,7,7,8,8,10]
target = 8
result = search(nums, target)
print(result)



# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]