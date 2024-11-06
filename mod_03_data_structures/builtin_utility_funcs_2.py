#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: additional_builtin_function_utilities
#
# Description: This program demonstrates additional built-in function
#              utilities in Python, such as `map()`, `filter()`, `all()`,
#              `any()`, `len()`, `abs()`, and `round()`. These functions
#              enable sequence processing, condition checks, and
#              basic mathematical operations.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Additional Built-in Function Utilities in Python ==========")
    demonstrate_map()
    demonstrate_filter()
    demonstrate_all_any()
    demonstrate_len_abs_round()

# Demonstrates the `map()` function
def demonstrate_map():
    numbers = [1, 2, 3, 4]
    print("\nUsing map() to square each number in the list:")
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Original numbers: {numbers}")
    print(f"Squared numbers: {squares}")

# Demonstrates the `filter()` function
def demonstrate_filter():
    numbers = [1, 2, 3, 4, 5, 6]
    print("\nUsing filter() to find even numbers in the list:")
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Original numbers: {numbers}")
    print(f"Even numbers: {evens}")

# Demonstrates the `all()` and `any()` functions
def demonstrate_all_any():
    values = [True, True, False]
    print("\nUsing all() and any() for condition checks:")
    print(f"Are all values True? {all(values)}")   # Returns False
    print(f"Is at least one value True? {any(values)}")  # Returns True

# Demonstrates the `len()`, `abs()`, and `round()` functions
def demonstrate_len_abs_round():
    text = "Hello, world!"
    number = -7.65
    print("\nUsing len(), abs(), and round() functions:")
    print(f"Length of text '{text}': {len(text)}")      # Length of string
    print(f"Absolute value of {number}: {abs(number)}")  # Absolute value
    print(f"Rounded value of {number}: {round(number, 1)}")  # Rounded to 1 decimal place

if __name__ == "__main__":
    main()
