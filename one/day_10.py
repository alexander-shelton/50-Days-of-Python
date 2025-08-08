#!/usr/bin/env python3
#
# Day 10: Hide my Password

def hide_password() -> str:
    user_psswd = input("Enter your password: ")
    hidden_password = '*' * len(user_psswd)
    print(f"Your password is {len(hidden_password)} characters long.")
    return hidden_password


# Extra Challenge: A Thousand Separator
def convert_numbers(nums: list) -> list:
    return [f"{num:,}" for num in nums]