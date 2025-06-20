# Problem 1: 
# Write a function sum_of_number_strings() that takes in a list of strings nums. 
# Each string is a representations of integers. 
# The function should return the sum of these strings as an integer.

def sum_of_number_strings(nums):
    sum = 0
    for i in nums:
        sum += int(i)
    return sum 

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
print('\n')


# sum = sum_of_number_strings(nums)
# print(sum)

# Problem 2:
# Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter 
# and removes all duplicates in the list. The function returns the modified list.

def remove_duplicates(nums):
    lst = list(set(nums))
    lst.sort()

    # for i in nums:
    #     if num not in lst:
    #         list.append(num)

    return lst

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
print('\n')


# def reverse_only_letters(s):
#     start = 0
#     new_str = " "

#     for end in range(len(s) -1, -1, -1):
