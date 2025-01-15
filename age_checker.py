#Age Checker
"""Write a program that asks user to check age and if age is greater than
or equal to 18 it display you are adult otherwise display You are young"""

def check_age():
    age = input("Please enter your age: ")
    age = int(age)
    if (age >= 18):
        return "You are adult"
    else:
        return "You are Young"

p_age = check_age()
print(p_age)