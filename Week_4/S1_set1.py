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

