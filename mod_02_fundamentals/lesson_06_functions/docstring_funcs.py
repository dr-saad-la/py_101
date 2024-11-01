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
    print("========== Docstrings and Documentation in Python ==========")
    print("This program demonstrates how to use docstrings to document functions.")
    print("*" * 80)

    # Call documented functions and display their docstrings
    print("Adding two numbers using the add function.")
    print(f"Result: {add(3, 5)}")
    print("\nDocstring for 'add' function:", add.__doc__)

    print("*" * 80)

# Basic function with a docstring
def add(a, b):
    """
    Return the sum of a and b.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

# Function with a more detailed docstring
def multiply(a, b):
    """
    Multiply two numbers and return the result.

    This function takes two numbers, a and b, and returns their product.
    It is commonly used in mathematical calculations where multiplication
    is required.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.

    Example:
        >>> multiply(3, 4)
        12
    """
    return a * b

# Function with no return value, but with a docstring for instructions
def display_message(message):
    """
    Display a message to the console.

    Args:
        message (str): The message to display.

    Example:
        >>> display_message("Hello, world!")
        Hello, world!
    """
    print(message)

if __name__ == "__main__":
    main()
