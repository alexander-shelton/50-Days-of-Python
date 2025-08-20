#!/usr/bin/env python3
#
# Day 41: Only Words with Vowels  

def words_with_vowels(words: str) -> list:
    return [word.lower() for word in words.split(' ') if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word]


## Extra Challenge: Class of Cars
class Car:
    def __init__(self, model: str, color: str, year: int, transmission: str, electric: bool):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
    
    def print_cars(self) -> str:
        # print(f"car_model = {self.model}\nColor = {self.color}\nYear = {self.year}\nTranmission = {self.transmission}\nElectric = {self.electric}")
        return f"car_model = {self.model}\
            \nColor = {self.color}\
            \nYear = {self.year}\
            \nTranmission = {self.transmission}\
            \nElectric = {self.electric}"

class Ford(Car):
    def __init__(self, model, color, year, transmission, electric):
        super().__init__(model, color, year, transmission, electric)

class BMW(Car):
    def __init__(self, model, color, year, transmission, electric):
        super().__init__(model, color, year, transmission, electric)

class Tesla(Car):
    def __init__(self, model, color, year, transmission, electric):
        super().__init__(model, color, year, transmission, electric)