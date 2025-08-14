#!/usr/bin/env python3
#
# Day 13: Pay Your Tax

def your_vat() -> float:
    while True:
        try:
            price = int(input("Enter the price of an item: "))
        except ValueError:
            print("Please enter a valid price. (e.g., 220)")
        try:
            vat = float(input("Enter the VAT: "))
            vat /= 100
        except ValueError:
            print("Please enter a valid VAT percentage. (e.g., 15)")
        if price and vat:
            return price + price * vat


## Extra Challenge: Pyramid of Snakes
import emoji

def python_snakes(num: int):
    for i in range(1, num+1):
        snakes = emoji.emojize(":snake:" * i)
        spacing = " " * (num - i)
        print(f"{spacing}{snakes}")