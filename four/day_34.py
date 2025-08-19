#!/usr/bin/env python3
# 
# Day 34: Just Digits

def just_digits(file) -> str:
    with open('python.csv', 'r') as file:
        return ', '.join([word for line in file.readlines() for word in line.split(' ') if word.isnumeric()])