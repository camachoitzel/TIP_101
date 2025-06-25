# Problem set 1

# subsequence
def is_subsequence(lst, sequence):
    # create empty list
    result = []
    # if sequence is empty return empty list
    if sequence == []:
        return []
    # iterate throuhg the list
    for num in lst:
        # if num is not in result
        if num not in result:
            # and if num is also in sequence list
            if num in sequence:
                # add number to result list
                result.append(num)
    # return whether the result equals the sequence w/ T or F
    # aka the list contains the sequence = T, F otherwise
    return result == sequence

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

# Create Dictionary

def create_dictionary(keys, values):
    # create empty dict
    result = {}

    # handles empty list
    if values == []:
        return result
    # use the length of the keys list as the num of times you iterate through the list
    for i in range(len(keys)):
        # insert the key at its same index in result dict w/ the value at that same index in values
        result[keys[i]]=  values[i]
    # return the completed dictionary
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
    # iterate through keys and values in restock_list
    for key, value in restock_list.items():
        # check if the keys in restock = current_inv
        if key in current_inventory:
            # if they are the same add its value to current inv
            current_inventory[key] += value
        else:
            # if different add the key and value to current inventory
            current_inventory[key] = value
    # return the updated inventory
    return current_inventory


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))

# Calculate GPA

def calculate_gpa(report_card):
    gpa = 0
    grading_scale = {"A": 4, "B": 3, "C": 2, "D": 1, "F":0}
    number_of_classes = len(report_card)

    # loops through the report_card dict
    for grade in report_card:
        # letter = the values in report card 1 by 1 b/c of the loop
        letter = report_card[grade]

        # checks if the letter value in report_card is in the key values of grading_scale
        if letter in grading_scale:
            # if it is then the value of gpa is updated to the value of that letter in grading_scale dict
            gpa += grading_scale[letter]
    # returns a float (rounded to 2 decimal places) of the calculated gpa / number of classes to get the true gpa
    return round(float(gpa / number_of_classes), 2)


report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

# Best Book 

def highest_rated(books):
    # create empty dict to return result
    highest_rated_book = {}
    # set the highest rating to neg infinity to compare values in the rating
    highest_rating = float('-inf')

    # iterate through each dictionary in the books list
    for book in books:
        # check if the value of highest_rating is less than or equal to the value help by the key "rating"
        if highest_rating <= book["rating"]:
            # if true set the highest_rating to the current rating being checked as it is now the highest
            highest_rating = book["rating"]
            # set highest_rated_book to the book we found to be the highest rated
            highest_rated_book = book
    # return highest_rated_book as a dict
    return highest_rated_book

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print("\n")

print(highest_rated(books))

# Index-Value Map
def index_to_value_map(lst):
    # create empty dict to return later
    index_to_value = {}

    # go through each index in the list
    # for i in range(len(lst)):
    #     # set the value at index i to the key "i"
    #     index_to_value[i] = lst[i]

    # or loop through the index and values
    for i, value in enumerate(lst):
        # set the key to the index at i and it's value to the value in the list
        index_to_value[i] = value
    return index_to_value


print("\n")
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))