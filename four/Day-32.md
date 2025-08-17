# Day 32:  Password Validator  

Write a function called `password_validator`. The function asks the user to enter a password. A valid password should have at least **one uppercase letter**, **one lowercase letter**, and **one number**. It should not be less than **8 characters long**. When the user enters a password, the function should check if the password is valid. If the password is valid, the function should return the valid password. If the password is not valid, the function should inform the user of the errors in the password and prompt the user to enter another password. The code should only stop once the user enters a valid password.  

## Extra Challenge: Valid Email  

```python
emails = [ "ben@mail.com ", "john@mail.cm ", "kenny@gmail.com ", "@list.com " ]
```

Write a function called `email_validator` that takes a list of emails and checks if the emails are valid. Only valid emails are returned by the function. A valid email address will have the following: the **@** symbol (if the @ sign is at the beginning of the name, the email is invalid). If there is more than one **@** sign, the email is invalid. All valid emails must end with a **dot com (.com)**; otherwise, the email is invalid. For example, the list of emails above should output the following as valid emails:  

```python
['ben@mail.com', 'kenny@gmail.com']
```

If no emails in the list are valid, the function should return "All emails are invalid."
