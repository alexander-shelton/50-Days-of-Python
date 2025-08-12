#!/usr/bin/env python3
#
# Day 15: Same in Reverse

def same_in_reverse(string: str) -> bool:
    return string == string[::-1]


## Extra Challenge: What’s My Age?
names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
def your_age() -> str:
    name = input("Enter your name: ")
    if name not in names_age.keys():
        while True:
            try:
                age = int(input("Enter your age: "))
                names_age[name] = age
                break
            except ValueError:
                print("Please enter a valid number. (e.g., 31)")
    else:
        age = names_age.get(name)
    return f"Hi, {name.capitalize()}, you are {age} years old."