#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: partial_functions
#
# Description: This program demonstrates the concept of partial functions
#              in Python. Partial functions allow you to fix specific
#              arguments for a function, creating a new function with fewer
#              arguments. They are especially useful for simplifying function
#              calls in data processing pipelines.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

from functools import partial

def main():
    print("========== Partial Functions in Python ==========")
    print("Partial functions allow you to fix specific arguments in a function.")
    print("This example demonstrates how to create customized power functions.")
    print("*" * 80)

    # Create a square function by fixing the exponent to 2
    square = partial(power, exponent=2)
    print("Square of 5:", square(5))  # Output: 25

    # Create a cube function by fixing the exponent to 3
    cube = partial(power, exponent=3)
    print("Cube of 4:", cube(4))  # Output: 64

    # Demonstrate practical application with converting measurements
    meters_to_kilometers = partial(convert_units, factor=0.001)
    print("5000 meters to kilometers:", meters_to_kilometers(5000))  # Output: 5.0

    grams_to_kilograms = partial(convert_units, factor=0.001)
    print("1500 grams to kilograms:", grams_to_kilograms(1500))  # Output: 1.5

    print("*" * 80)

# Function that calculates power given a base and exponent
def power(base, exponent):
    """
    Raises the base to the power of exponent.
    """
    return base ** exponent

# Function for unit conversion using a factor
def convert_units(value, factor):
    """
    Converts units by multiplying the value by a conversion factor.
    """
    return value * factor

if __name__ == "__main__":
    main()
