"""
Makhai Morgan
Sep 15, 2025
lab 5, functions
"""

"""
- pre-defined function: Pythin library
- user defined fucntion: create by the programmer

what is function?
- block of code that begins with 'def' follows by the name of the function and parentheses():
- The body of the function is indented after the : 
- The body of the function only runs when the function is called.
- To call a function, we need to write the functions name and parentheses
"""
# import Python file
from lab5_Morgan_function import *

# call function product()
print("\n----- Example 1: intro function -----")
n1 = 2
n2 = 5
p = product(n1,n2)
print(f"The product of {n1} and {n2} is {p}")
p = product()
print(f"The product is {p}")
p = product(5)
print(f"The product is {p}")

print("\n----- Example 2: function to calculate the hypotenuse -----")
s1 = 5
s2 = 3
hyp = hypotenuse(s1, s2)
print(f"The hypotenuse is {hyp:0.2f}")

print("\n----- Example 3: function to check if the number is positive, negative, or zero.  -----")
c = check_number(-3)
print(f"The number is {c}")
c = check_number(5)
print(f"The number is {c}")
c = check_number(0)
print(f"The number is {c}")

print("\n----- Example 4: function to calculate the average of a list of grades, and return 'true' if the avaerage is greater than 60, otherwise, it returns 'false'  -----")
grades = [50, 60, 85, 93, 72, 98]
avg = check_grades(grades)
print(f"Did I pass the class? {avg}")
grades = [50, 60, 30, 50]
print(f"Did I pass the class? {check_grades(grades)}")

print("\n----- LAB EXERCISE  -----")
random = 4
print(f"Did I guess the number right? Random guess number: {random}")
guess = guess_number(random)

random = 20
print(f"Did I guess the number right? Random guess number: {random}")
guess = guess_number(random)

random = 10
print(f"Did I guess the number right? Random guess number: {random}")
guess = guess_number(random)