#!/usr/bin/env python3
#
# Day 38: Guess a Number  

from random import randint

def guess_a_number():
    num = randint(0, 10)
    count = 3
    while count > 0:
        while True:
            try:
                guess = int(input("Guess a number between 1-10: "))
                break
            except ValueError:
                print("Please guess a valid number.")
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        elif guess == num:
            print("Correct")
            break
        count -= 1    
    return "You are a winner!" if guess == num else "You are a loser!"
    
        
## Extra Challenge: Find Missing Numbers  
def missing_numbers(nums: list) -> list:
    return [i for i in range(nums[0], nums[-1] + 1) if i not in nums]