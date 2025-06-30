# def move_zeros(nums):
#     left = 0
#     for right in range(len(nums)):
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#     return nums

# nums = [0,1,0,3,12]
# print(move_zeros(nums))

# def find_middle(lst):
#     slow=fast=0
#     while fast < len(lst) and fast + 1 < len(lst):
#         slow += 1
#         fast += 2
#     return lst[slow]

# list = [1,2,3,4,5,6]
# print(find_middle(list))

# def find_pair_sum(s, target):
#     nums = []

#     for char in s:
#         nums.append(int(char))
    
#     for i in range(len(nums) - 1):
#         left = i
#         right = i + 1
#         if nums[left] + nums[right] == target:
#             return True
#     return False

# s= "1234"
# target = 5

# print(find_pair_sum(s, target))

def find_min_sublist_sum(nums, k):
    if k > len(nums):
        return 0
    
    min_sum = float('inf')
    
    for i in range(len(nums) - k + 1):
        left = i
        right = i + k
        sub_sum = 0
        for j in range(left, right):
            sub_sum += nums[j]
        if sub_sum < min_sum:
                min_sum = sub_sum
    return min_sum

nums = [5, -1, 3, 2, -4]
k = 2

print(find_min_sublist_sum(nums, k))