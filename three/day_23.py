#!/usr/bin/env python3
#
# Day 23: Simple Calculator

def calculator():
    operations = {
        "a": {"name": "ADD", "symbol": "+"}, 
        "s": {"name": "SUBTRACT", "symbol": "-"}, 
        "d": {"name": "DIVIDE", "symbol": "/"}, 
        "m": {"name": "MULTIPLY", "symbol": "*"}
    }
    while True:
        operation = input("Select an operation: [ a | s | d | m ]: ").lower()
        if operation in ('a', 's', 'd', 'm'):
            ask = input(f"You selected {operations.get(operation)['name']}, is this correct? [Y/n]: ")
            if ask == "" or ask in ("Y", "y"):
                operation = operations.get(operation)['symbol']
                break
        print("Enter a valid operation. (e.g., a | s | d | m)")
    
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Enter a valid number.")

    if operation == '+':
        result = num1 + num2
        return f"{num1} {operation} {num2} = {result}"
    elif operation == '-':
        result = num1 - num2
        return f"{num1} {operation} {num2} = {result}"
    elif operation == '/':
        try:
            result = num1 / num2
            return f"{num1} {operation} {num2} = {int(result)}"
        except ZeroDivisionError:
            return "Sorry you can not divide a number by 0"
    elif operation == '*':
        result = num1 * num2
        return f"{num1} {operation} {num2} = {result}"
        
## Extra Challenge: Multiply Words
from string import ascii_uppercase

def multiply_words(string: str) -> str:
    words = string.split(' ')
    total = 1
    string_words = []
    for word in words:
        if word.lower() == word:
            total *= len(word)
            string_words.append(f"{word} ({len(word)})")
    return f"{total}: {', '.join(string_words)}" 