# Problem 1: Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# return True if the input string is valid and False otherwise.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
from collections import deque

def is_valid(s):
    stack = []
	




# Example #1:
# Input: s = "()"
# Expected Output: True

# Example #2:
# s = "()[]{}"
# Expected Output: True

# Example #3: 
# s = "(())"
# Expected Output: True

# Example #4:
# s = "(]"
# Expected Output: False

# Example #5:
# s = "([)]"
# Expected Output: False

# Problem 2: Best Time to Buy & Sell Stock
# You are given a list of integers prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def max_profit(prices):
    left = 0
    right = len(prices) - 1
    max_profit = 0
    while left < right + 1 and left != len(prices) - 1:
        buy_price = prices[left]
        sell_price = prices[right]
        profit = sell_price - buy_price
        if profit > max_profit:
            max_profit = profit
        right -= 1
        if left == right:
            left += 1
            right = len(prices) - 1
    return max_profit

print(max_profit([7,6,4,3,1]))
print(max_profit([7,1,5,3,6,4]))

# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example #2:
# Input: prices = [7,6,4,3,1]
# Expected Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Problem 3: Shuffle Merge
# Given the heads of two singly linked lists of integers, 
# merge their nodes to make one list, taking nodes alternately between the two lists. 
# If either list runs out of elements before the other, all nodes from the list with remaining nodes should be appended onto the end of the merged list. 
# Return the head of the merged list.

class Node:
    def __init__(self, value, next):
        self.val = value
        self.next = next

def shuffle_merge(head_a, head_b):
    # if a is empty return b
    if not head_a:
        return head_b
    # if b is empty return a
    if not head_b:
        return head_a
    
    # start a list for the merged nodes with beggining of head_a
    merged_list = head_a
    # set the pointer to the current node in head_a to head_a.next
    current_a = head_a.next
    # current pointer at b is at the beggining of head_b
    current_b = head_b
    # set the pointer for where in the merged list we are to the beggining of the list
    curr_merged = merged_list
    
    # use toggle to determine if we are advancing the a or b pointers
    toggle = True
    # while the lists for a and b are not empty
    while current_a and current_b:
        # if toggle is True
        if toggle:
            # set the next node in the merged list to the current node in the pointer current_b
            curr_merged.next = current_b
            # advance the pointer in current_b to the next so the loop continues until the end of the list
            current_b = current_b.next
        # if toggle is not true
        else:
            # we are in list a and we set the next node in the merged list to waht the current_a pointer holds
            curr_merged.next = current_a
            # advance the current_a pointer to the next node to continue loop
            current_a = current_a.next
        # advance the pointer in the merged list to be ready for the next input from either a or b
        curr_merged = curr_merged.next
        # set toggle to false if true and true if false to switch between lists a and b
        toggle = not toggle
    # if one list is longer than the other then attache the rest of the values to the merged_list
    curr_merged.next = current_a if current_a else current_b
    # return the head of the merged list
    return merged_list



# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4 —> 5 —> 6
# Input: head_a = 1, head_b = 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 5 —> 3 —> 6

# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 3
