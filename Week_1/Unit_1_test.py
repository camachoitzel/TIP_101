
def find_sum(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum

input1 = [1,2,3,4,5]
output1 = find_sum(input1)

print(output1)

def find_min(lst):
    min = lst[0]

    for i in lst:
        if min > i:
            min = i
    return min

input2 = [5,1,2,3,4]
output2 = find_min(input2)

print(output2)