# Hello User

def greet_user(name):
    return ("Hello " + name + "\n")

print(greet_user("Michael"))

# Calculate the difference
def difference(a, b):
    return b - a

print(difference(3,8))
print("\n")

# List concatenation
def concatenate_list(nums):
    length = len(nums)
    ans = [None] * (2 * length)
    for i in range(length):
        ans[i] = nums[i]
        ans[i + length] = nums[i]
    return ans

list = [1,2,3,4]
new_list = concatenate_list(list)
print(new_list)
print("\n")