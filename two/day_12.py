#!/usr/bin/env python3
#
# Day 12: Count the Dots
from datetime import datetime

def count_dots(string: str) -> int:
    return string.count('.')


## Extra Challenge: Your Age in Minutes
def age_in_minutes():
    current_year = datetime.now().year
    while True:
        try:
            age = int(input("Enter the year you were born: "))
        except ValueError:
            print(f"Please enter a valid year (e.g., {current_year - 120} - {current_year}).")
        if age > current_year:
            print(f"Please enter a valid year (e.g., {current_year - 120} - {current_year}).")
        elif (current_year - age) > 120:
            print(f"Please enter a valid year (e.g., {current_year - 120} - {current_year}).")
        else:
            break
    total_minutes = ((((current_year - age) * 365) * 24) * 60)
    return f"You are {total_minutes:,} minutes old."