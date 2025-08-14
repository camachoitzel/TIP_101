# Unit 1 Set 2

# Write a function greet_user() that takes in a string name as a parameter and prints "Hello <name>".

def greet_user(name):
    print("Hello " + name)

name = "Michael"
greet_user(name)


# Write a function difference() that returns the difference between two integers a and b (b should be subtracted from a).

def difference(a, b):
    return (b - a)

diff = difference(3,8)
print(diff)

# Given an integer list nums of length n, create a function concatenate_list() 
# that creates and returns a list ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums lists.
def concatenate_list(nums):
    n = len(nums)
    lst = [0] * (2*n)

    for i in range(0, len(nums)):
        lst[i] = nums[i]
        lst[i + n] = nums[i]

        

    return lst
nums = [1,2,3,4]
nums_2 = []
nums_3 = [5]

print(concatenate_list(nums))
print(concatenate_list(nums_2))
print(concatenate_list(nums_3))

# Write a function sleep_assessment() 
# that takes in an integer parameter hours indicating the number of hours the user slept.
# If hours is less than 8, print "Oof, go back to bed!".
# If hours is greater than or equal to 8 and less than or equal to 10, print "You got a good night's rest!".
# If hours is greater than 10, print "You're a sleep prodigy!".

def sleep_assessment(hours):
    if hours < 8 :
        print("Oof, go back to bed!")
    
    elif hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    
    elif hours > 10:
        print("You're a sleep prodigy!")

    

sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)
sleep_assessment(-10)


# Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
# If service_quality is "poor", the function should return 10% of the bill value.
# If service_quality is "average", the function should return 15% of the bill value.
# If service_quality is "excellent", the function should return 20% of the bill value.
# If service_quality is any other value, the function should return None.

def calculate_tip(bill, service_qual):
    if service_qual is "poor":
        return bill * 0.10
    
    elif service_qual is "average":
        return bill * 0.15
    
    elif service_qual is "excellent":
        return bill * 0.20
    
    else:
        return None


tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)

# Write a function rock_paper_scissors() that determines the winner of a game of Rock, Paper, Scissors. 
# The function accepts two strings as parameters: player1 and player2. 
# Each parameter can have a value of "rock", "paper", or "scissors".

# Print either "Player 1 wins!" or "Player 2 wins!" according to the following rules:
# Rock wins against scissors.
# Scissors wins against paper.
# Paper wins against rock.

# If both player1 and player2 have the same value, print "It's a tie!".

def rock_paper_scissors(player1, player2):
    lst = ["rock", "paper", "scissors"]
    if player1 == player2:
        print("It's a tie!")
    
    elif player1 == "rock":
        if player2 == "paper":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    
    elif player1 == "scissors":
        if player2 == "rock":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    

    else:
        if player2 == "scissors":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")