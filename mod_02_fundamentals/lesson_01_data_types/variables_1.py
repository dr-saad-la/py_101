#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: variables
#
# Description:
# A simple demonstration of creating and using variables in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("Example: Creating variables")
    create_vars()
    
    print("Example: Reassign Variables")
    reassign_variables()

def create_vars():
    """
    Creates and displays different types of variables.
    """
    
    age = 24                                # integer value
    distance = 52.3                         # float value
    name = "Anas"                           # string value
    course = "Statistics"                   # String
    is_valid = True                         # boolean
    print(f"The age is: {age}")
    print(f"The distance is: {distance}")
    print(f"The  is: {name}")
    print(f"The course name is: {course}")
    print(f"Is the value valid: {is_valid}")
    
def reassign_variables():
    # Reassign variables
    name = "Amir"
    age = 28
    is_valid = False
    
    # Print updated values
    print(f"Name: {name}, Age: {age}, Premium Member: {is_valid}")
    
    # Variables Reassignments
    
    name = "Adam"
    age = 30
    is_valid = False
    
    print("Variables after reassignments")
    print("*"*52)
    
    print(f"Name: {name}, Age: {age}, Premium Member: {is_valid}")

if __name__ == "__main__":
    main()
