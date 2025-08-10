# Problem 1: Contains Duplicates
# Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

# def contains_duplicate(nums):
#     # dict to hold the times a num has been seen
#     seen = {}

#     # for loop to go through the numbers in nums
#     for num in nums:
#         # check if that num us in the dict
#         if num in seen:
#             # if you have seen it then increase it's count by 1 in the dict
#             seen[num] += 1
#             # if the count after updating == 2 then you have fouind a duplicate
#             if seen[num] == 2:
#                 return True
#         # num is not in the dict yet so set its count to 1
#         else:
#             seen[num] = 1
#     # no duplicates found
#     return False


# nums = [1,2,3,1]
# print(contains_duplicate(nums))

# nums1 = [1,2,3,4]
# print(contains_duplicate(nums1))

# nums2 = [1,1,1,3,3,4,3,2,4,2]
# print(contains_duplicate(nums2))

# Problem 2: Remove Element
# Given a list of integers nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, for your response to be acceptable, you need to do the following things:

# Change the list nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.

# Return k

def remove_elem(nums, val):
    # counter for num of elems in list
    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


nums = [3,2,2,3] 
val = 3

print(remove_elem(nums, val))
print(nums)