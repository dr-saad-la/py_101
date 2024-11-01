#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Function Definitions
#
# Description: This program demonstrates defining functions in Python,
#              including basic functions, type-annotated functions, and
#              functions with detailed docstrings. Also demonstrates a
#              real-world function for parsing full names.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("=========== Introduction to Functions ===========")

    # Simple function with no arguments or docstring
    print("Simple Function without Arguments:")
    simple_func()

    # Simple function with arguments and a NumPy-style docstring
    print("\nGreeting Example with NumPy-style Docstring:")
    print(greet("Nassim"))

    # Function with type annotations
    print("\nFunction with Type Annotations:")
    print(f"Call {calculate_square.__name__} with arg = 4 is {calculate_square(4)}")

    # Real-World Example: Name Parsing Function
    print("\nReal-World Example: Name Parsing Function")
    name = "Dr. Saad LAOUADI"
    title, first_name, middle_name, last_name = parse_full_name(name)
    print(f"Title: {title}, First Name: {first_name}, Middle Name: {middle_name}, Last Name: {last_name}")

    print("=" * 80)


# Basic function without docstring or arguments
def simple_func():
    print("This is a simple function with no arguments or return value.")


# Simple function with a NumPy-style docstring
def greet(name):
    """
    Greet a user with a personalized message.

    Parameters
    ----------
    name : str
        The name of the person to greet.

    Returns
    -------
    str
        A greeting message that includes the user's name.
    """
    return f"Hello, {name}!"


# Function with type annotations
def calculate_square(number: int) -> int:
    """
    Calculate the square of a given number.

    Args:
        number (int): The number to square.

    Returns:
        int: The square of the input number.
    """
    return number * number


# Function to parse a full name into title, first name, middle name, and last name
def parse_full_name(full_name: str) -> tuple:
    """
    Parse a full name into its components: title, first name, middle name, and last name.

    Parameters
    ----------
    full_name : str
        The full name of the person.

    Returns
    -------
    tuple
        A tuple containing the title, first name, middle name, and last name.
    """
    parts = full_name.split()  # Split the name into parts
    title = parts[0] if parts[0].endswith('.') else None
    first_name = parts[1] if title else parts[0]
    last_name = parts[-1]
    middle_name = " ".join(parts[2:-1]) if len(parts) > 3 else None
    return title, first_name, middle_name, last_name


if __name__ == "__main__":
    main()