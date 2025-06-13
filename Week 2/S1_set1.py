# Problem set 1

# subsequence
def is_subsequence(lst, sequence):
    # create empty list
    result = []

    if sequence == []:
        return []
    for num in lst:
        if num not in result:
            if num in sequence:
                result.append(num)
    return result == sequence

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

# Create Dictionary

def create_dictionary(keys, values):
    result = {}
    if values == []:
        return result
    for i in range(len(keys)):
        result[keys[i]]=  values[i]
    return result

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

# Print Pair

def print_pair(dictionary, target):
    # check if target in dictionary
    if target not in dictionary:
        print("That pair does not exist!")
    else:
        # print the key + target
        print("Key: " + target)
        # print value + dictionary
        print("Value: " + dictionary.get(target))

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

# Keys vs Values

def keys_v_values(dictionary):
    # initialize variables for the sums
    sum_keys = sum(dictionary.keys())
    sum_values = sum(dictionary.values())
    # if key sums are greater than value sums print 'keys'
    if sum_keys > sum_values:
        return "keys"
    # otherwise values are greater than keys therfore print 'values'
    elif sum_keys < sum_values:
        return "values"
    # if they are equal then return balanced
    else:
        return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

# Restock Inventory
def restock_inventory(current_inventory, restock_list):
    pass