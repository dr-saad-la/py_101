#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: sequences
#
# Description: A demonstration of working with sequence types (list, tuple, range)
# in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_ranges()


def demonstrate_lists() -> None:
    """
    Demonstrates how to work with lists in Python.
    """
    # List example: A list of colors
    colors = ["red", "green", "blue"]
    print(f"Variable 'colors' has value: {colors} and type: {type(colors)}")
    print(f"The first color in the list is: {colors[0]}")  # Accessing the first element
    colors.append("yellow")
    print(f"After adding a new color, 'colors' is now: {colors}\n")  # Demonstrating mutability


def demonstrate_tuples() -> None:
    """
    Demonstrates how to work with tuples in Python.
    """
    # Tuple example: A tuple representing a 2D point
    point = (2, 3)
    print(f"Variable 'point' has value: {point} and type: {type(point)}")
    print(f"The x-coordinate of the point is: {point[0]}")  # Accessing the first element
    print("Tuples are immutable; attempting to change 'point' would raise an error.\n")


def demonstrate_ranges() -> None:
    """
    Demonstrates how to work with ranges in Python.
    """
    # Range example: A range representing numbers from 1 to 9
    numbers = range(1, 10)
    print(f"Variable 'numbers' has value: {list(numbers)} and type: {type(numbers)}")
    print("Range objects are commonly used in loops, for example:")
    for num in numbers:
        print(num, end=' ')
    print("\n")  # Adding newline for better output readability


if __name__ == "__main__":
    main()
