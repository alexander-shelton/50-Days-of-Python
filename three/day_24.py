#!/usr/bin/env python3
# 
# Day 24: Average Calories  

def average_calories() -> float:
    calories = []
    while True:
        calorie = input(f"Enter the calories for day {len(calories)} or type 'done' to quit: ")
        if calorie == 'done':
            break
        else:
            try:
                calories.append(int(calorie))
            except ValueError:
                print("Calories must be a valid number.")
    return sum(calories) / len(calories)

## Extra Challenge:  Create a Nested List
def nested_lists(*args: list) -> list:
    for arg in args:
        if type(arg) != list:
            return "Invalid arguments. Please check your arguments."
    return [arg for arg in args]