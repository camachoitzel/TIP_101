# Problem 1: Neatly Nested
# Given a string, return True if it is a nesting of zero or more pairs of parentheses. 
# Return False otherwise. A valid pair of parentheses is defined as (). 
# The input string will only contain the characters ( or ). Your solution must be recursive.
# Evaluate the time and space complexity of your solution.

def is_nested(paren_s):
	if paren_s == "":
		return True
	if paren_s[0] == "(" and paren_s[-1] == ")" and len(paren_s) >=2:
		return is_nested(paren_s[1:-1])
	
	return False

print(is_nested("(())"))

# Problem 2: How Many 1s
# Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.

def count_ones(lst):
