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
    Return the sum of a and b.

    Parameters
    ----------
    a : int or float
        The first number to be added.
    b : int or float
        The second number to be added.

    Returns
    -------
    int or float
        The sum of `a` and `b`.

    Example
    -------
    >>> add(3, 5)
    8
    """
    return a + b

def multiply(a, b):
    """
    Multiply two numbers and return the result.

    This function multiplies two numbers, `a` and `b`, and returns the result.
    It is commonly used in mathematical calculations requiring multiplication.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The product of `a` and `b`.

    Example
    -------
    >>> multiply(3, 4)
    12
    """
    return a * b

def display_message(message):
    """
    Display a message to the console.

    Parameters
    ----------
    message : str
        The message to display on the console.

    Example
    -------
    >>> display_message("Hello, world!")
    Hello, world!
    """
    print(message)

if __name__ == "__main__":
    main()
