#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: callable_objects_and_call
#
# Description: This program demonstrates the use of callable objects in Python.
#              By implementing the __call__ method, objects can act like functions,
#              allowing for functional, object-oriented design and custom behaviors.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Callable Objects in Python ==========")
    print("This program demonstrates how objects can be made callable by defining a __call__ method.\n")

    # Create instances of callable classes and demonstrate their behavior
    multiplier = Multiplier(3)
    print(f"Calling multiplier(10) results in: {multiplier(10)}")  # Multiplies by 3

    adder = Adder(5)
    print(f"Calling adder(10) results in: {adder(10)}")  # Adds 5

    print("\nExamples of using callable objects in a functional manner:\n")
    print(f"Using multiplier in a map function: {list(map(multiplier, [1, 2, 3, 4]))}")
    print(f"Using adder in a map function: {list(map(adder, [10, 20, 30, 40]))}\n")


# Class that acts like a function to multiply by a fixed number
class Multiplier:
    """
    Callable class to multiply a given number by a fixed multiplier.

    Args:
        factor (int or float): The fixed multiplier.
    """
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        """Multiply the input by the fixed factor."""
        return self.factor * value


# Class that acts like a function to add a fixed number
class Adder:
    """
    Callable class to add a fixed number to the given input.

    Args:
        increment (int or float): The fixed number to add.
    """
    def __init__(self, increment):
        self.increment = increment

    def __call__(self, value):
        """Add the fixed increment to the input."""
        return self.increment + value


if __name__ == "__main__":
    main()
