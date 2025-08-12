#!/usr/bin/env python3
#
# Day 14: Flatten the List

def flat_list(nested_list: list) -> list:
    return [nested_list[i][j] for i in range(len(nested_list)) for j in range(len(nested_list[i]))]
    #
    # Visualize the list comprehension:
    # return [
    #     nested_list[i][j]
    #     for i in range(
    #         len(nested_list)
    #     ) 
    #     for j in range(
    #         len(nested_list[i])
    #     )
    # ]

## Extra Challenge: Teacher’s Salary
def your_salary() -> str:
    name = input("Enter the teacher's name: ")
    while True:
        try:
            periods = int(input("Enter the number of periods taught this month: "))
        except ValueError:
            print("Please enter a valid number of periods. (e.g., 105)")
        try:
            monthly_rate = int(input("Enter the monthly rate: "))
        except ValueError:
            print("Please enter a valid monthly rate. (e.g., 20)")
        if name and periods and monthly_rate:
            if periods > 100:
                total_pay = 100 * monthly_rate
                total_pay += (periods - 100) * (monthly_rate * 1.25)
            else:
                total_pay = periods * monthly_rate
            return f"Teacher: {name}\nPeriods: {periods}\nGross salary: {int(total_pay):,}"