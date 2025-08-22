#!/usr/bin/env python3
#
# Day 42: Spelling Checker  
from  textblob import TextBlob

def spelling_checker() -> str:
    while True:
        word = input("Enter a word: ")
        if word != TextBlob(word).correct():
            question = input(f"Did you mean "
                             f"{TextBlob(word).correct()}? "
                             f"type yes/no : ")
            if question == 'yes':
                break
            else:
                print("Please try again.")
        elif word == TextBlob(word).correct():
            break
    return f"Your word is, {TextBlob(word).correct()}"


## Extra Challenge: Set Alarm
import pygame
import datetime
from time import sleep


def set_alarm():
    while True:
        hour = input("Please enter the hour (0-23): ")
        if hour.isdigit() and 0 <= int(hour) <= 23:
            break
        print("Invalid hour. Please enter valid hour.")
    
    while True:
        minute = input("Please enter the minute (0-59): ")
        if minute.isdigit() and 0 <= int(minute) <= 23:
            break
        print("Invalid minute. Please enter valid minute.")
    
    alarm_time = "{:02d}:{:02d}".format(int(hour), int(minute))
    print("You have set an alarm for", alarm_time)
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('noise.wav')

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if alarm_time == now:
            print("Wake up")
            print("Wake up")
            print("Wake up")
            sound.play()
            pygame.event.wait()
            sleep(5)
            break 