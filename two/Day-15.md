# Day 15: Same in Reverse

Write a function called `same_in_reverse` that takes a string and
checks if the string reads the same in reverse. If it is the same, the
code should return __True__ if not, it should return __False__. For
example, __"dad"__ should return __True__, because it reads the same in
reverse.  

## Extra Challenge: What’s My Age?

Write a function called `your_age`. This function asks a student to
enter their name, and then it returns their age. For example, if a
user enters __Peter__ as their name, your function should return, __"Hi,
Peter, you are 27 years old."__ This function reads data from the
database (dictionary below). If the name is __not__ in the dictionary,
your code should tell the user that their name is not in the
dictionary and ask them for their age. Your code should then add
the __name__ and __age__ to the dictionary named __"names_age"__ below.
Once added, your code should return to the user, __"Hi, (name),
you are (age) years old."__ Remember to convert the input from
the user to lowercase letters.

```python
names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter":   27}
```
