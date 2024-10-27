#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: type_checking
#
# Description:
#  A demonstration of using the type() function to check the data type of
#  different variables in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    check_variable_types()


def check_variable_types() -> None:
    """
    Demonstrates how to use the type() function to check the type of various variables.
    """
    # Integer example
    age = 30
    print(f"Variable 'age' has value: {age} and type: {type(age)}")

    # Float example
    price = 19.99
    print(f"Variable 'price' has value: {price} and type: {type(price)}")

    # String example
    language = "Python"
    print(f"Variable 'language' has value: {language} and type: {type(language)}")

    # List example
    fruits = ["apple", "banana", "cherry"]
    print(f"Variable 'fruits' has value: {fruits} and type: {type(fruits)}")

    # Boolean example
    is_valid = True
    print(f"Variable 'is_valid' has value: {is_valid} and type: {type(is_valid)}")

    # Complex number example
    complex_number = 3 + 5j
    print(f"Variable 'complex_number' has value: {complex_number} and type: {type(complex_number)}\n")


if __name__ == "__main__":
    main()