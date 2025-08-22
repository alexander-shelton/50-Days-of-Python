#!/usr/bin/env python3
#
# Day 44: Save Emails

def save_emails() -> str:
    emails = open_emails()
    with open('emails.csv', 'a') as f:
        while True:
            email = input("Enter an email or 'done' to quit: ")
            if email == 'done':
                break
            if email not in emails:
                f.write(f"{email}")
                f.write('\n')
    return "Emails saved to file 'emails.csv'"
    

def open_emails() -> str:
    with open('emails.csv', 'r') as f:
        lines = f.readlines()
        emails = [line.strip() for line in lines]
        return emails