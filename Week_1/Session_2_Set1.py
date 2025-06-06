# Problem 1:
# print list
# step 1 : use a for loop to go through list
# step 2: print item in list

def print_list(lst):
    for i in lst:
        print(i)

lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

# Problem 2
# print doubled list
# step 1 : use a for loop to go through list
# step 2: print item in list * 2

def doubled(lst):
    for i in lst:
        print(i * 2)

lst = [1,2,3]
doubled(lst)

# Problem 3
# return doubled list
# step 1: create empty list
# step 2: use a for loop to go through list
# step 3: double items in list
# step 4: append doubled items to empty list
# step 5: return new list

def doubled(lst):
    result = []
    for i in lst:
        result.append(i * 2)
    return result

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)

# Problem 4
# Flip Signs
# step 1: create empty list
# step 2: use a for loop to go through list
# step 3: multiply items by -1
# step 4: append items to new list
# step 5: return new list

def flip_sign(lst):
    result = []
    for i in lst:
        result.append(i * -1)
    return result

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

# Problem 5
# Max Diff
# step 1: create variables to hold min and max
# step 2: for loop to iterate through list
# step 3: two if statements to check for max and min
# step 4: return max and min
# step 5: calculate difference between max and min

def max_difference(lst):
    max = lst[0]
    min = lst[0]

    for i in lst:
        if max < i:
            max = i

        if min > i:
            min = i
    
    return max - min

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
print("\n")

# Problem 6
# Below threshold
# step 1: initialize count var
# step 2: loop through the list
# step 3: check if num > threshold
# step 4: if so increase count
# step 5: return count

def count_less_than(numbers, threshold):
    # step 1: initialize an empty list
    count = 0
    # step 2: loop through each num in lst
    for num in numbers:
        # step 3: check if num > threshold
        if num < threshold:
            # step 4: if so add to new list
            count = count + 1
    return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

# Problem 7
# Evens List
# step 1: create an empty list
# step 2: iterate through list
# step 3: 
