# Instructor Demo
# anagrams

def group_anagrams(words):
    # 1. create empty dictionary
    anagram = {}
    # 2. loop thorugh words
    for word in words:
        # 3.sort the word to create a key
        key = ''.join(sorted(word))
        # 4. if the key not in dict, create a new list
            # "aet": []
        if key not in anagram:
            anagram[key] = []
        # 5. add word to group
        anagram[key].append(word)
            # "aet" : ["whatever word"]
    # return the grouped lists
    return list(anagram.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

# Print Pair