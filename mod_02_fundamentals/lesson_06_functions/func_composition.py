#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: function_composition
#
# Description: This program demonstrates function composition in Python.
#              Function composition allows combining multiple functions
#              to build more complex behaviors and operations.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Function Composition in Python ==========")
    print("This program demonstrates how to compose multiple functions for complex operations.\n")

    # Composing functions for a data pipeline example
    result = data_pipeline("  Hello World!  ")
    print(f"Data Pipeline Result: {result}")

    # Chaining mathematical operations
    composed_result = compose(square, double)(3)
    print(f"Result of squaring and then doubling 3: {composed_result}\n")


# Basic function to strip and lowercase a string
def clean_text(text: str) -> str:
    """Strips whitespace and converts text to lowercase."""
    return text.strip().lower()

# Function to reverse a string
def reverse_text(text: str) -> str:
    """Reverses the given text."""
    return text[::-1]

# Function to replace spaces with hyphens
def hyphenate_text(text: str) -> str:
    """Replaces spaces in the text with hyphens."""
    return text.replace(" ", "-")

# Function demonstrating function composition by chaining data cleaning functions
def data_pipeline(text: str) -> str:
    """
    Applies a series of transformations to the input text.

    Args:
        text (str): The input text to process.

    Returns:
        str: Transformed text after applying clean_text, reverse_text, and hyphenate_text.
    """
    return hyphenate_text(reverse_text(clean_text(text)))


# Function that composes two functions (f and g)
def compose(f, g):
    """
    Returns a composed function that applies g and then f.

    Args:
        f (function): The outer function to apply.
        g (function): The inner function to apply.

    Returns:
        function: A function that represents f(g(x)).
    """
    return lambda x: f(g(x))

# Example mathematical functions for composition
def square(x: int) -> int:
    """Returns the square of x."""
    return x * x

def double(x: int) -> int:
    """Doubles the input x."""
    return x * 2


if __name__ == "__main__":
    main()
