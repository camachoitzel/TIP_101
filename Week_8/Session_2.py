# Mock Interview Question

# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Understand: we are given a lowercase string and need to return the first letter that appears twice
# Should use a dictionary with a counter to store the number of times a letter is seen
# when a letter's count == 2 then return that letter

def appears_twice(s):
    # create an empty dictionary to add the letters as they are seen
    seen = {}
    # loop through the char in the string
    for char in s:
        # check if the char is not in the dict
        if char not in seen:
            # if not then add it to the dict w/ val = 1
            seen[char] = 1
        # if the char is in the dict
        else:
            # increase it's val by 1
            seen[char] += 1
            # check if the value == 2 aka we have seen it twice
            if seen[char] == 2:
                # if we have immeadiately return that char and stop looking at the rest of the string
                return char
    # if there are no chars that appear twice return None
    return None

s = "abcdd"
print(appears_twice(s))
# Output: "d"
s_2 = "abccbaacz"
print(appears_twice(s_2))
s_3 = "abcdacd"
print(appears_twice(s_3))

s_4 = "abcde"
print(appears_twice(s_4))
# Output: "c"