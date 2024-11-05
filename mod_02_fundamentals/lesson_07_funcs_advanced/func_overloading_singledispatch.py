#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: function_overloading_singledispatch
#
# Description: Demonstrates function overloading in Python using
#              functools.singledispatch, allowing different versions
#              of a function to be executed based on the type of input.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

from functools import singledispatch

def main():
    print("========== Function Overloading with singledispatch ==========")
    print("This program demonstrates function overloading based on input type using functools.singledispatch.")
    print("*" * 80)

    # Testing different overloads
    print("Calling process with an integer:")
    process(10)  # Expected to call the int version

    print("\nCalling process with a string:")
    process("Hello")  # Expected to call the string version

    print("\nCalling process with a list:")
    process([1, 2, 3])  # Expected to call the list version

    print("*" * 80)

# Base function with singledispatch decorator
@singledispatch
def process(value):
    """
    Default process function that handles unsupported types.

    Args:
        value: Any unsupported type.

    Returns:
        None
    """
    print(f"Processing {type(value).__name__}: Type not supported by process function.")

# Overload for integer type
@process.register(int)
def _(value):
    """
    Process function specialized for integers.

    Args:
        value (int): The integer to process.

    Returns:
        None
    """
    print(f"Processing integer: {value ** 2}")  # Example: Squaring the integer

# Overload for string type
@process.register(str)
def _(value):
    """
    Process function specialized for strings.

    Args:
        value (str): The string to process.

    Returns:
        None
    """
    print(f"Processing string: {value.upper()}")  # Example: Converting to uppercase

# Overload for list type
@process.register(list)
def _(value):
    """
    Process function specialized for lists.

    Args:
        value (list): The list to process.

    Returns:
        None
    """
    print(f"Processing list: Sum is {sum(value)}")  # Example: Summing up the list elements

if __name__ == "__main__":
    main()
