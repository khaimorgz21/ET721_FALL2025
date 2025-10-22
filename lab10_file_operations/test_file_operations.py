"""
Makhai Morhgan
Oct 17, 2025
Lab 10, file operation test
"""
import unittest
import os
from file_operations import read_file, write_file, append_file

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test
        self.filename = "test_file.txt"
        self.msg = "Makhai Morgan"
    
    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        # test writing text to a file
        msg = "Makhai Morgan"
        with open(self.filename, "w") as f:
            f.write(msg)

        # verify file exits and content matches
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result,msg)

    def test_read_file(self):
        # test reading text from a file
        expected_content = "Read me!"
        with open(self.filename, "w") as f:
            f.write(expected_content)

        with open(self.filename, "r") as f:
            data = f.read()

        self.assertEqual(data, expected_content)

    def test_append_file(self):
        # test appending text to an existing file
        initial_content = "Line one"
        append_content = "\nLine two"

        with open(self.filename, "w") as f:
            f.write(initial_content)

        with open(self.filename, "r") as f:
            f.write(append_content)

        with open(self.filename, "r") as f:
            final_data = f.read()

        self.assertEqual(final_data, initial_content + append_content)

    # EXERCISE
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

    unittest.main()