"""
Create a Python file called path_practice.py.
Task: Write a program that:
Gets the current working directory.
Joins it with a filename called main.py.
Checks whether that file exists.
Checks whether the resulting path is a file or directory.
Prints its absolute path.
"""

import os

# 1. Get current working directory
current_dir = os.getcwd()

print("Current directory:", current_dir)

# 2. Join directory with filename
filename = "main.py"

full_path = os.path.join(current_dir, filename)

print("Full path:", full_path)

# 3. Check whether file exists
if os.path.exists(full_path):
    print("Path exists!")

else:
    print("Path does not exist!")

# 4. Check file or directory
if os.path.isfile(full_path):
    print("It is a file.")

elif os.path.isdir(full_path):
    print("It is a directory.")

else:
    print("Neither file nor directory exists.")

# 5. Absolute path
absolute_path = os.path.abspath(full_path)

print("Absolute path:", absolute_path)