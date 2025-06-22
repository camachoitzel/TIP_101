def char_count(str):
    lowercase = str.lower()
    result = {}

    for char in lowercase:
        if char == ' ':
            continue
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result


input = 'Hello World'
print(char_count(input))

def ransom_note(message, magazine):
    mag_list = list(magazine)
    
    for char in message:
        if char in mag_list:
            mag_list.remove(char)
        else:
            return False
    
    return True




message = "a"
magazine = "b"

print(ransom_note(message, magazine))