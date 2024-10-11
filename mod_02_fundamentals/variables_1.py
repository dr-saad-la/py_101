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
    
    age = 24            # integer value
    distance = 52.3     # float value
    name = "Anas"          # string value
    course = "Statistics"  # String
    is_valid = True             # boolean
    print(f"The age is: {age}")
    print(f"The distance is: {distance}")
    print(f"The course name is: {name}")
    print(f"Is the value valid: {is_valid}")
    
def reassign_variables():
    # Reassign variables
    person_name = "Amir"
    age = 28
    is_member = False
    
    # Print updated values
    print(f"Name: {person_name}, Age: {age}, Premium Member: {is_member}")

if __name__ == "__main__":
    main()
