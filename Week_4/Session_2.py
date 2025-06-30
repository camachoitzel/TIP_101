# Instructor Demo
# 

# Given a string 's' determine of it can become a palindrome by removing at most one character

def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    deletion = False

    while left < right:
        if s[left] == s[right]:
            
            left += 1
            right -= 1
        # if the chars are not equal and no characters have been deleted
        elif not deletion:
            deletion = True
            left += 1
        else:
            break
    
    else:
        return True
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

        else:
            return False
    
    return True
        
s = "abca"
print(valid_palindrome(s))
