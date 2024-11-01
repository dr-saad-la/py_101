#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: false_values_check
#
# Description: This program demonstrates how to check for "falsy" values
#              in Python. It examines various values and prints whether
#              they evaluate to True or False in a boolean context.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Checking False Values in Python ==========")
    print("This program checks common values in Python to determine if they evaluate to False.")
    print("*" * 80)

    # Define a list of values to check
    values_to_check = [
        None,
        False,
        0,
        0.0,
        "",
        [],
        {},
        (),
        set(),
        range(0),
        "Non-empty string",
        [1, 2, 3],
        {"key": "value"},
        (1,),
        42
    ]

    # Check each value and determine if it is False in a boolean context
    for value in values_to_check:
        check_false_value(value)

    print("*" * 80)

def check_false_value(value):
    """
    Checks if a given value evaluates to False and prints the result.

    Args:
        value: The value to check for "falsiness."
    """
    # Check if the value evaluates to False
    if not value:
        print(f"The value {repr(value)} is considered False.")
    else:
        print(f"The value {repr(value)} is considered True.")

if __name__ == "__main__":
    main()
