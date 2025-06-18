# Strings

# name = "hello world"
# print("original string:" , name)

# print("First character:" , name[0])

# print("Lastcharacter:" , name[-1])

# print("First 5 charcaters:" , name [:5])

# print("Characters from index 6 onwards:" , name[6:])

# print("Length of the string:", len(name))

# print("Uppercase:", name.upper())

# print("Lowercase", name.lower())

# print("Replacing 'world' with 'Python'", name.replace("world", "Python"))

# Instructor Demo: Longest Substring
# Write a function that takes in a string s and returns the length of the longest substring without repeating characters.

# 1. initialize a set to track characters
# 2. initilaize left and max_lenght to 0
# 3. for each char at position right
# 4. while char is in set
# 5. remove s[left] from set
# 6. move left forward
# 7. add s[right] to set
# 8. update max length

def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if len(seen) > 1:
            max_length = max(max_length, right - left + 1)
    return max_length

# once a letter repeats the streak is broken
s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

# substring = 0 if all the letters are the same
s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)