"""
Rolls as many dice as the user wants
"""

import random

def roll_dice(n):
    """
    Returns n dice values from 1 to 6
    """
    rolled_dice = []
    for i in range(n):
        rolled_dice.append(random.randint(1,6))

    final_statement = "Dice Rolled: "
    for dice in enumerate(rolled_dice):
        if dice[0] == 0:
            final_statement += str(dice[1])
        elif dice[0] == len(rolled_dice) - 1:
            final_statement += f", and {str(dice[1])}"
        else:
            final_statement += f", {str(dice[1])}"
    
    return final_statement
        

def number_of_dice():
    """
    Returns the number of dice the user would like to roll
    """
    while True: 
        try:
            rolls = int(input("How many dice would you like to roll? ").strip())
            return rolls
        except ValueError: 
            print("Please enter an integer.")

def keep_playing():
    """
    Allows the user to infinitely roll the dice
    """
    while True:
        answer_one = input("Would you like to roll again? (Y/N): ")
        if answer_one == "yes" or answer_one == "y":
            print(roll_dice(number_of_dice()))
        elif answer_one == "no" or answer_one == "n":
            break
        else:
            print("That is not an accepted answer. Please try again.")

#Starts the dice rolling
while True:
    answer_one = input("Would you like to roll the dice? (Y/N): ").lower().strip()
    if answer_one == "yes" or answer_one == "y":
        print(roll_dice(number_of_dice()))
        keep_playing()
        break
    elif answer_one == "no" or answer_one == "n":
        break
    else: 
        print("That is not an accepted answer. Please try again.")

