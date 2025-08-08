#!/usr/bin/env python3
#
# Day 5: My Discount

from collections import Counter

def my_discount():
    while True:
        try:
            price = int(input("Enter the price: "))
            break
        except ValueError:
            print("Please enter the price as a number.")
    while True:
        try:
            discount = int(input("Enter the discount: "))
            break
        except ValueError:
            print("Please enter the discount as a number.")
    return price - price * (discount / 100)


# Extra Challenge: Tuple of Student Sex
def count_student_gender(students: list):
    students = [s.lower() for s in students]
    counter = Counter(students)
    return [(key.capitalize(), val) for key, val in counter.items()]

