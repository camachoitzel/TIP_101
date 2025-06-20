# Instructor Demo
# Write a function wordPattern() that takes in a string pattern and a string s as parameters. 
# The function returns True if s follows the pattern and False otherwise. 
# The string follows the pattern if there is a 1:1 correspondence between a letter in the pattern and a non-empty word in s.

def word_Pattern(pattern, s):
    # 1. split s into list of words
    words = s.split
    # 2. if lenght of words != lenght of pattern: return False
    if len(words) != len(pattern):
        return False
    # 3. create a char_to_word and word_to_char dict
    char_to_word = {}  # map pattern characters to words
    word_to_char = {}  #map words to pattern character

    # 4. for each char, word in (pattern,words)
    for char, word in zip(pattern, words):
        # 5. if char in char_to_word
        if char in char_to_word:
            # if current mapping != return false
            if char_to_word[char] != word:
                return False
        # 6. else add dict
        else: 
                char_to_word[char] != word
        # 7. repeat 4-6 but word_to_char
        if word in word_to_char:
            if word_to_char[char] != word:
                return False
        else:
             word_to_char[char] != word
    # return True
    return True

pattern = "abba"
s = "dog cat cat dog"
print(word_Pattern(pattern, s))
s2 = "dog cat cat fish"
print(word_Pattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(word_Pattern(pattern2, s3))
s4 = "dog dog dog dog"
print(word_Pattern(pattern2, s4))
