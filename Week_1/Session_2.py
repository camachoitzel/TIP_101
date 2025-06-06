# Instructor Demo
def above_threshold(lst, threshold):
    # step 1: initialize an empty list
    result = []
    # step 2: loop through each num in lst
    for num in lst:
        # step 3: check if num > threshold
        if num > threshold:
            # step 4: if so add to new list
            result.append(num)
    # step 5: return the list
    return result

lst = [8,2,13,11,4,10,14]
threshold = 10

empty_lst = []

print(above_threshold(lst, threshold))
print(above_threshold(empty_lst, threshold))