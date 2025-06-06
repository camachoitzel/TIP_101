import emoji

# today's menu
def todays_mood():
    mood = "pizza"
    print("Today's mood: " + mood)

todays_mood()

# Lunch Menu

def print_menu(menu):
    print("Lunch today is: " + menu)

my_menu = "🍕"
print("\n")
print_menu(my_menu)

# sum of 2 ints
def sum(a, b):
    return a + b

sum = sum(13, 27)

print("\n")
print(sum)

sum_doubled = sum * 2

print(sum_doubled)

# product of 2 ints
def product(a, b):
    return a * b

print(product(22,7))

# Classify Age

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"

output = classify_age(18)
print("\n")
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output + "\n")

# What time is it
def what_time_is_it( hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"
    
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time + "\n")

# Blackjack

def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust")
    elif score >= 17 or score > 21:
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)
print("\n")

# First Item

def get_first(lst):
    return lst.pop(0)

my_list = [3,1,6,7,5]
print(get_first(my_list))
print("\n")

# Last Item
def get_last(lst):
    return lst.pop(len(lst) - 1)

my_list_1 = [3,1,6,7,5]
print(get_last(my_list_1))
print("\n")

# Counter

def counter(num):
    for i in range(num + 1):
        print(i)

counter(7)
print("\n")

# Sum of  1-10

def sum_ten():
    num = 10
    sum_num = 0
    for i in range(num + 1):
        sum_num = sum_num + i
    
    return sum_num

output = sum_ten()
print(output)
print("\n")

# Total sum
def sum_positive_range(stop):
    sum_num = 0
    for i in range(stop + 1):
        sum_num += i
    return sum_num

sum = sum_positive_range(6)
print(sum)
print("\n")

# Total Sum in range

def sum_range(start , stop):
    sum_num = 0
    for i in range(start, stop + 1):
        sum_num = sum_num + i
    
    return sum_num

sum = sum_range(3 , 9)
print(sum)
print("\n")

# Negative Numbers

def print_negatives(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            print(lst[i])
        
print_negatives([3,-2,2,1,-5])
print("\n")