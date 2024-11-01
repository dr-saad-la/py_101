#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: truthy_values_check
#
# Description: This program demonstrates how to check for "truthy" values
#              in Python. It examines various values to see if they evaluate
#              to True in a boolean context.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Checking Truthy Values in Python ==========")
    print("This program checks various values in Python to determine if they evaluate to True.")
    print("*" * 80)

    # Define a list of values to check for truthiness
    values_to_check = [
        True,
        1,
        3.14,
        "Non-empty string",
        [1, 2, 3],
        {"key": "value"},
        (1,),
        set([1, 2, 3]),
        range(1, 5),
        CustomObject(),
        "False"  # Even a non-empty string with the text 'False' is truthy
    ]

    # Check each value and determine if it is True in a boolean context
    for value in values_to_check:
        check_truthy_value(value)

    print("*" * 80)

# Custom class to demonstrate truthy objects
class CustomObject:
    """
    A custom class that represents a truthy object in Python.
    """
    def __bool__(self):
        # Custom object is always truthy by returning True
        return True

    def __repr__(self):
        return "CustomObject()"

# Function to check if a value is truthy
def check_truthy_value(value):
    """
    Checks if a given value evaluates to True and prints the result.

    Args:
        value: The value to check for "truthiness."
    """
    # Check if the value evaluates to True
    if value:
        print(f"The value {repr(value)} is considered True.")
    else:
        print(f"The value {repr(value)} is considered False.")

if __name__ == "__main__":
    main()
