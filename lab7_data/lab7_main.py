"""
Makhai Morgan
Lab 7, accesing data in a file
Oct 14, 2025
"""

from lab7_function import *

testing()
print("\n ---- example 1: reading file -----")
read_data("phrases.txt")

print("\n ---- example 2: reading specific portion of a file -----")
read_up("phrases.txt")

print("\n ---- example 3: reading specific portion using readline -----")
read_readline("phrases.txt")

print("\n ---- example 4: reading specific portion using readlines -----")
read_all("phrases.txt")

print("\n ---- example 5: loop through each line -----")
read_each("phrases.txt")

print("\n ---- example 6: creating a new file -----")
new_file("Morgan.txt")

print("\n ---- example 7: append data into an existing file -----")
stamp_date("Morgan.txt")

print("\n ---- EXERCISE -----")
count_yahoo = email_read("user_email.txt", "@yahoo")
count_email = email_read("user_email.txt", "@gmail")
count_hotmail = email_read("user_email.txt", "@hotmail")
