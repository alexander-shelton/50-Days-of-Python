# Day 10: Hide my Password

Write a function called `hide_password` that takes no parameters. The function takes an input (a password) from a user and returns a hidden password. For example, if the user enters "hello" as a password, the function should return " \* \* \* \* \* " as a password and tell the user that the password is __5 characters__ long.

## Extra Challenge: A Thousand Separator

Your new company has a list of figures saved in a database. The issue is that these numbers have no separator. The numbers are saved in a list in the following format:

__\[1000000, 2356989, 2354672, 9878098].__

You have been asked to write a code that will convert each of the numbers in the list into a __string__. Your code should then add a comma to each number as a __thousand separator__ for readability. When you run your code on the above list, your output should be:

__\[ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]__

Write a function called `convert_numbers` that will take one argument, the list of numbers above.
