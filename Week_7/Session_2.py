# Mock Interview

# Problem #1
# Given a string s consisting of lowercase and/or uppercase English letters and digits, 
# return all possible strings that can be formed by changing the case of the letters in s. 
# You may not alter the order of characters in the string, and digits should remain unchanged.

# Input: s = "a1b2"
# Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
# Input: s = "3z4"
# Output: ["3z4", "3Z4"]
# Input: s = "12345"
# Output: ["12345"]

# 1. To create an empty list
# 2. for loop to loop through the string
# 3. append original at start
# 4. append all uppercase at end of the string 