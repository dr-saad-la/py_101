#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: function_annotations_01
#
# Description: Demonstrates the use of function annotations in Python.
#              This program shows how to attach metadata to function
#              parameters and return values, providing better documentation
#              and clarity for function usage.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Function Annotations in Python ==========")
    print("Function annotations provide a way to attach metadata to parameters and return values.")
    print("This can enhance code clarity and assist in type checking.")
    print("*" * 80)

    # Basic example of function annotations
    print("1. Basic Function with Annotations")
    number = 5
    print(f"The square of {number} is: {calculate_square(number)}")
    print("*" * 80)

    # Real-world example of function annotations
    print("2. Real-World Example with Annotations")
    length, width = 10.5, 7.2
    print(f"The area of a rectangle with length {length} and width {width} is: {calculate_area(length, width)}")
    print("*" * 80)


# Function to calculate the square of a number with annotations
def calculate_square(number: int) -> int:
    """
    Calculate the square of a given number.

    Args:
        number (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    return number * number


# Real-world example: Function to calculate the area of a rectangle
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.
    """
    return length * width


if __name__ == "__main__":
    main()