# Instructor Demo
# 

# Given a string 's' determine of it can become a palindrome by removing at most one character

def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    deletion = False
    found_palindrome = False

    while left < right:
        if s[left] == s[right]:
            
            left += 1
            right -= 1
        elif not deletion:
            deletion = True
            left += 1

        if left >= right:
            found_palindrome = True
        else:
            break
        
    left = 0
    right = len(s) - 1
    deletion = False

    while left < right:
        if s[left] == s[right]:
            
            left += 1
            right -= 1
        elif not deletion:
            deletion = True
            right += 1

        if left >= right:
            found_palindrome = True

        else:
            return False
    
    return found_palindrome
        
s = "abcca"
print(valid_palindrome(s))