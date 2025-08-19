#!/usr/bin/env python3
#
# Day 39: Password Generator  
from string import ascii_letters, punctuation 
from random import randint

all_chars = [str(i) for i in range(10)] + [char for char in ascii_letters] + [char for char in punctuation]

def generate_password() -> str:
    strength = input("Enter how strong you'd like the password to be.\nEnter 1 for weak, 2 for strong, or 3 for very strong: ")
    password = []
    if strength == '1':
        while len(password) < 5:
            password.append(all_chars[randint(0, len(all_chars)-1)])
        return ''.join(password)
    elif strength == '2':
        while len(password) < 8:
            password.append(all_chars[randint(0, len(all_chars)-1)])
        return ''.join(password)
    elif strength == '3':
        while len(password) < 12:
            password.append(all_chars[randint(0, len(all_chars)-1)])
        return ''.join(password)
    else:
        return "Invalid option. Please try again and select a valid option. e.g. 1, 2, 3"