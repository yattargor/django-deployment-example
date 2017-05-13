###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

import random
#GET GUESS
def get_guess():
     return list(input("What's your guess"))

#GENERATE RANDOM/COMPUTER CODE NUMBERS
def generate_code():
    digits = [str[num] for num in range(10)]
    random.shuffle(digits)
    #grab only three
    return digits[-3:]

#CLUES REPORT
def generate_clues(code, user_guess):
    if user_guess == code:
        print("CODE CRACKED")

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        print("Nope")
    else
        return clues

#RUN GAME LOGIC
print("Welcome in my game!")
secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED":
    guess = get_guess()

    clue_report = generate_clues(secret_code, guess)
    for clue in clue_report:
        print(clue)
