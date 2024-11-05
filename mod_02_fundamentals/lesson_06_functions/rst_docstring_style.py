#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: docstrings_documentation
#
# Description: This program demonstrates the use of docstrings for documenting
#              functions in Python. Docstrings provide an accessible way to
#              understand the purpose and usage of each function.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    """
    Demonstrates usage of docstrings in Python functions.

    This function serves as the main entry point for the program, displaying
    the purpose of each function and calling the documented functions with
    sample inputs to showcase their usage.
    """
    print("========== Docstrings and Documentation in Python ==========")
    print("This program demonstrates how to use docstrings to document functions.")
    print("*" * 80)

    # Call documented functions and display their docstrings
    print("Adding two numbers using the add function.")
    print(f"Result: {add(3, 5)}")
    print("\nDocstring for 'add' function:", add.__doc__)

    print("Multiplying two numbers using the multiply function.")
    print(f"Result: {multiply(3, 4)}")
    print("\nDocstring for 'multiply' function:", multiply.__doc__)

    print("Displaying a message using the display_message function.")
    display_message("Hello, world!")
    print("\nDocstring for 'display_message' function:", display_message.__doc__)

    print("*" * 80)

def add(a, b):
    """
    Return the sum of two numbers.

    :param a: The first number to add. Can be an integer or float.
    :type a: int or float
    :param b: The second number to add. Can be an integer or float.
    :type b: int or float
    :return: The sum of `a` and `b`.
    :rtype: int or float

    :Example:

    >>> add(3, 5)
    8
    """
    return a + b

def multiply(a, b):
    """
    Multiply two numbers and return the result.

    This function takes two inputs, `a` and `b`, and returns their product.
    It is commonly used in mathematical calculations where multiplication
    is required.

    :param a: The first number.
    :type a: int or float
    :param b: The second number.
    :type b: int or float
    :return: The product of `a` and `b`.
    :rtype: int or float

    :Example:

    >>> multiply(3, 4)
    12
    """
    return a * b

def display_message(message):
    """
    Display a message to the console.

    :param message: The message to display.
    :type message: str

    :Example:

    >>> display_message("Hello, world!")
    Hello, world!
    """
    print(message)

if __name__ == "__main__":
    main()
