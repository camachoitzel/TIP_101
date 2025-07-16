# Problem 1: Hello Hello
# A recursive function is a function that calls itself within the body of the function.
# Step 1: Copy the recursive function repeat_hello() into Replit and run it.
# Step 2: Then create another function repeat_hello_iterative() that produces the same output without using recursion.
# Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)

def repeat_hello_iterative(n):
	while n > 0:
		print("Hello")
		n -= 1
repeat_hello(5)


# Problem 2: Factorial Cases
# Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. 
# The factorial of a number is the product of all numbers between 1 and n.
# Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.
# Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.

def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)

result = factorial(5)
print(result)

# Problem 3: Recursive Sum
# Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.
# What is the time complexity of this function? What is the space complexity?

def sum_list(lst):
	if not lst:
		return 0
	# add the 1st element and add it to the new list that does not include the 1st element
	# each recursive call returns a shorter list missing the first element 
	# keep going until you get an empty list
	return lst[0] + sum_list(lst[1:])

lst = [1,2,3,4,5]
print(sum_list(lst))

# Problem 4: Recursive Power of 2
# Given an integer n, return True if n is a power of two. Otherwise, return `False``.
# An integer n is a power of two if there exists an integer x such that n == 2ˣ.
# Solve the problem recursively. What is the time complexity of this function? What is the space complexity?

def is_power_of_two(n):
	# powers of 2 cannot be neg
	if n <= 0:
		return False
	# 1 = 2^0 which is still a power of 2
	if n == 1:
		return True
	# if n is divisible by 2
	if n % 2 == 0:
		# divide n by 2 over and over until you get 1 which hits base case
		return is_power_of_two(n // 2)
	# if n is not divisible by 2 then it is not a power of 2
	return False

print(is_power_of_two(4))
print(is_power_of_two(3))
	
	
	
