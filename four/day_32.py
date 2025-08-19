#!/usr/bin/env python3
# 
# Day 32:  Password Validator  

def password_validator():
    while True:
        password = input("Enter a password: ")
        requirements = {'lowercase': False, 'uppercase': False, 'number': False, 'length': False}
        if len(password) > 8:
            requirements['length'] = True
        for char in password:
            if char.islower():
                requirements['lowercase'] = True
            elif char.isupper():
                requirements['uppercase'] = True
            elif char.isnumeric():
                requirements['number'] = True
        for k, v in requirements.items():
            if not v:
                print(f"Password does not meet requirement {k}")
        if requirements['length'] and requirements['lowercase'] and requirements['uppercase'] and requirements['number']:
            return password
        

## Extra Challenge: Valid Email
def email_validator(emails: list) -> list:
    valid_emails = []
    for email in emails:
        email_parts = email.split('@')
        if len(email_parts[0]) > 1:
            if len(email_parts) == 2:
                second_half = email_parts[1]
                if len(second_half) >= 5:
                    if second_half[-4:] == '.com':
                        valid_emails.append(email)
    return valid_emails if len(valid_emails) > 1 else "All emails are invalid."