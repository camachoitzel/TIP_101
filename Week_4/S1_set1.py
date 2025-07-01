# Prime Number
# Write a function is_prime() that takes in a positive integer n 
# and returns True if it is a prime number and False otherwise. 
# A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n):

    if n < 2:
        return False
    

    for i in range(2,n-1):
       if n % i == 0:
           return False
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))


# Two-pointer Reverse List
# Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. 
# The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
# use 2 pointer approach

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    for i in range(len(lst) - 1):
        temp = left
        left = right
        right = temp
        left += 1
        right -= 1

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))