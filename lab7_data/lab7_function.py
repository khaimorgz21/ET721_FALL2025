"""
Makhai Morgan
Lab 7, accesing data in a file (functions)
Sep 29, 2025
"""
def testing():
    print("Makhai Morgan")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line in a file with a python code
    fileuser =open(filename, 'r')

    # use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)