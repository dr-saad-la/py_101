#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: hello_world
#
# Description:
# This script demonstrates the classic "Hello, World!" program in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    say_hello()

def say_hello():
    print("Hello world!")

# Other information
# Check the predefined variables by python
print(dir())

# The module name
print(f"The script (module) name: {__name__}")

# The file name
print("The file name", __file__)

if __name__ == "__main__":
    main()
