#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: built_in_function_utilities_advanced
#
# Description: This program demonstrates additional built-in function
#              utilities in Python, such as `zip()`, `enumerate()`,
#              `reversed()`, `sorted()`, `sum()`, `min()`, and `max()`.
#              These functions help with sequence processing, iteration,
#              and basic aggregation.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Advanced Built-in Function Utilities in Python ==========")
    demonstrate_zip()
    demonstrate_enumerate()
    demonstrate_reversed()
    demonstrate_sorted()
    demonstrate_sum_min_max()

# Demonstrates the `zip()` function
def demonstrate_zip():
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 78]
    print("\nUsing zip() to combine names and scores:")
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

# Demonstrates the `enumerate()` function
def demonstrate_enumerate():
    items = ["apple", "banana", "cherry"]
    print("\nUsing enumerate() to iterate with indices:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

# Demonstrates the `reversed()` function
def demonstrate_reversed():
    letters = ["a", "b", "c", "d"]
    print("\nUsing reversed() to iterate in reverse order:")
    for letter in reversed(letters):
        print(letter, end=" ")
    print()

# Demonstrates the `sorted()` function
def demonstrate_sorted():
    numbers = [5, 1, 8, 3, 2]
    print("\nUsing sorted() to sort a list of numbers:")
    print(f"Original list: {numbers}")
    print(f"Sorted list: {sorted(numbers)}")

# Demonstrates `sum()`, `min()`, and `max()` functions
def demonstrate_sum_min_max():
    numbers = [10, 20, 5, 30, 15]
    print("\nUsing sum(), min(), and max() to aggregate values:")
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")      # Sum of all numbers
    print(f"Min: {min(numbers)}")      # Smallest number
    print(f"Max: {max(numbers)}")      # Largest number

if __name__ == "__main__":
    main()
