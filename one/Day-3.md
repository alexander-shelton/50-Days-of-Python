# Day 3: Register Check

Write a function called `register_check` that checks how many students are in school. The function takes a dictionary as an argument. If the student is in school, the dictionary says "yes." If the student is not in school, the dictionary says "no." Your function should return the number of students in school. Using the dictionary below, your function should return **3**.

```Python
register = {'Michael': 'yes', 'John': 'no', 
   'Peter': 'yes', 'Mary': 'yes'}
```

## Extra Challenge: Lowercase Names

```Python
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
```

You are given a list of names above. This list is made up of names with **lowercase** and **uppercase** letters. Your task is to write a code that will return a **tuple** of all the names in the list that **only**
have **lowercase** letters. Your tuple should have names sorted alphabetically in descending order. Using the list above, your code should return:

```Python
('kerry', 'dickson', 'carol', 'adam')
```
