# Instructor Demo
def count_by_category(items):
    # 1. create empty dict
    counts = {}
    # 2. loop though each tuple
    for category, __ in items:
        # 3. if category is in dict, increment count
        if category in counts:
            counts[category] += 1
        # 4. else add cat to dict w/val of 1
        else:
            counts[category] = 1
    # 5. return the dict
    return counts

items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
print(count_by_category(items))