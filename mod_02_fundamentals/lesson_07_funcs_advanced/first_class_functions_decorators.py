#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: first_class_functions_closures
#
# Description: Demonstrates first-class functions and closures in Python.
#              The program shows how to use closures to encapsulate data
#              and create factory functions.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== First-Class Functions and Closures in Python ==========")
    print("This program demonstrates first-class functions and practical closures.")
    print("*" * 80)

    # Using a function as a first-class citizen
    print("Function as first-class citizen example:")
    square = get_square_function()
    print(f"Square of 5: {square(5)}")

    # Using closures for data encapsulation
    print("\nClosure example for encapsulating data:")
    counter = create_counter()
    print(counter())  # Output: 1
    print(counter())  # Output: 2
    print(counter())  # Output: 3

    print("*" * 80)


# Function that returns another function (First-Class Function example)
def get_square_function():
    """
    Returns a function that calculates the square of a number.

    Returns:
        function: A function that takes a number and returns its square.
    """
    return lambda x: x * x


# Function demonstrating a closure
def create_counter():
    """
    A closure that encapsulates a count variable.

    Returns:
        function: A function that increments and returns the count.
    """
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


# Factory function example using closures
def create_greeting(greeting):
    """
    A factory function that creates a greeting function with a preset greeting message.

    Args:
        greeting (str): The greeting message to use.

    Returns:
        function: A function that takes a name and returns a personalized greeting.
    """
    def greet(name):
        return f"{greeting}, {name}!"

    return greet

if __name__ == "__main__":
    main()

    # Demonstrating the factory function
    print("\nFactory function example with closures:")
    hello_greet = create_greeting("Hello")
    print(hello_greet("Alice"))  # Output: Hello, Alice!
    print(hello_greet("Bob"))    # Output: Hello, Bob!
