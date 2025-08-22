#!/usr/bin/env python3
#
# Day 43: Student Marks  

from string import punctuation, digits

def student_marks() -> dict:
    marks_dict = {}
    while True:
        try:
            name = input("Enter the students name or 'done' when finished: ").lower()
            if not name.isalpha():
                raise NameError("Please enter a valid name.")
            if name == 'done':
                break
            marks = int(input("Enter the students marks: "))
            if marks_dict.get(name):
                marks_dict[name].append(marks)
            else: 
                marks_dict[name] = [marks]
        except (NameError, ValueError) as e:
                print(f"Error: {e}")
    return marks_dict