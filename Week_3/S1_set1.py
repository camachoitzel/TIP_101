import string
# Problem 1

def count_mississippi(limit):
    for num in range(1, limit + 1):
        print( f"{num} mississippi")

count_mississippi(5)

# Problem 2
# Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
    if len(my_str) < 2:
        return my_str
    
    new_str = my_str[-1] + my_str[1:-1] + my_str[0]

    return new_str



my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)



# Problem 3
# Write a function is_pangram() that takes in a string my_str as a parameter 
# and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
    alphabet = set("abcdefghijklmnopqrstuv")


    lower = set(my_str.lower())

    return alphabet <= lower

# def is_pangram(myStr):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in myStr.lower():
            return False
    return True


my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

# Problem 4
# Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    # initalize empty string
    new_str = ""
    count = len(my_str)
    
    for i in my_str:
        new_str = i + new_str
        
    return new_str


my_str = "live"
print(reverse_string(my_str))

# Problem 5
# Write a function first_unique_char() that given a string my_str as a parameter, 
# it finds the first non-repeating character in it and returns its index. 
# If it does not exist, then return -1

def first_unique_char(my_str):
    seen = ""
    for i in my_str:
        while i not in seen:
            seen = my_str[i]
        

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))