# Day 12: Count the Dots

Write a function called `count_dots`. This function takes a string
separated by dots as a parameter and counts how many dots are in
the string. For example, __"h.e.l.p."__ should return 4 dots, and
__"he.lp."__ should return 2 dots.

## Extra Challenge: Your Age in Minutes

Write a function called `age_in_minutes` that tells a user __how
old they are in minutes.__ Your code should ask the user to enter
their __year of birth__, and it should return their age in minutes (by
subtracting their year of birth from the current year). Here are
things to look out for:

a. The user can only input a __4-digit__ year of birth. For example,
1930 is a valid year. However, entering any number longer
or shorter than 4 digits, should render the input invalid.
Notify the user that they must enter a four-digit number.

b.  If a user enters a year __before__ 1900, your code should tell
the user that the input is invalid. If the user enters the year
__after__ the current year, the code should tell the user to input
a valid year.

The code should __run until the user inputs a valid year__. Your
function should return the user's age in minutes. For example, if
someone enters 1930 as their year of birth, your function should
return:
__You are 48,355,200 minutes old.__
