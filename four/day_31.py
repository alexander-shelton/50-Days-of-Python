#!/usr/bin/env python3
# 
# Day 31: Longest Word

def longest_word(words: list) -> list:
    return [len(max(words, key=len)), max(words, key=len)]


## Extra Challenge: Create User
def create_user():
    login_info = {}
    while True:
        name = input("Enter your name: ")
        login_info['name'] = name
        while True:
            try:
                age = int(input("Enter your age: "))
                login_info['age'] = age
                break
            except ValueError:
                print("Please enter a valid number.")
        password = input("Enter your password: ")
        login_info['password'] = password
        print("User saved.")
        break
    while True:
        try:
            login_info.get(input("Enter your name: "))
            login_info.get(input("Enter your password: "))
            return "Logged in successfully"
        except KeyError:
            print("Wrong password or user name, please try again.")
    