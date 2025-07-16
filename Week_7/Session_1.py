# Instructor Demo

def resursive_sum(num):
    if num <= 1:
        return num
    return num + resursive_sum(num -1)

result = resursive_sum(5)
print(result) #output will be 15

# iterative sum
def iterative_sum(num):
    result = 0

    while num > 0:
        result += num
        num -= 1
    return result

iter_result = iterative_sum(5)
print(iter_result)

# getting a factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
fac_result = factorial(5)
print(fac_result)