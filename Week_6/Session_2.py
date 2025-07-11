# Instructor Demo (Mock interview Problem)

# Problem #1
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Examples:
# Input: s = "leetcode"
# Output: 0
# Input: s = "loveleetcode"
# Output: 2
# Input: s = "aabb"
# Output: -1

def find_nonrepeat(word):
    # make empty dict
    result = {}

    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    
    if 1 not in result.values():
        return -1
    
    for each, count in result.items():



s = "leetcode"
find_nonrepeat(s)
