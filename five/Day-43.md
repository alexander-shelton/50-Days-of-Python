# Day 43: Student Marks  

Write a function called `student_marks` that records the marks achieved by students in a test. The function should ask the user to input the name of the student and then ask the user to input the marks achieved by the student. The information should be stored in a dictionary. The **name** is the **key**, and the **mark** is a **value**. When the user enters "done," the function should return a dictionary of the names and values entered or an empty dictionary if no values are entered. Your code should ensure that:

- If a name contains punctuation characters **(!"#$%&'()*+, -./:;<=>?@[ \]^_`{|}~ )** or **numbers (digits)** your code should raise a **NameError** and ask the user to enter a valid name.
- If the a user enters invalid values for **value**, your code should handle the **ValueError**.
- Your code should run until a valid values are inputted.
