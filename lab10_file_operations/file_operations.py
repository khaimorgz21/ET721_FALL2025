"""
Makhai Morhgan
Oct 17, 2025
Lab 10, file operation test
"""


def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)


def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()


def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added.")


# function from exercise lab 7 (yesterday)
"""
create a function, named email_read(), that reads a txt file and returns
the number of users that have @gmail, @yahoo, and @hotmail email address. 
The function should have try-exception statement. 
You can test the function using the file&nbsp;user_email.txt file. 
"""


def email_read(filename, email):
    count_email = 0
    with open(filename, "r") as file1:
        filelines = file1.readlines()
        # loop through each item in 'filenames'
        for eachline in filelines:
            print(eachline.strip())
            if email in filename:
                email = "@yahoo"
                count_email += 1
                return count_email
        print(count_email)


email_read()
