#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: recursive_functions
#
# Description: Demonstrates the concept of recursive functions in Python.
#              Recursive functions are used to solve problems that can be
#              divided into smaller, similar sub-problems. Examples include
#              calculating factorials, Fibonacci numbers, and traversing
#              nested data structures.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Recursive Functions in Python ==========")
    print("Recursive functions call themselves to solve sub-problems within a larger problem.")
    print("*" * 80)

    # Factorial calculation
    print("Factorial Example:")
    print(f"5! = {factorial(5)}")  # Output: 120

    # Fibonacci series example
    print("\nFibonacci Series Example:")
    for i in range(6):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

    # Traversing a nested data structure example
    print("\nNested Data Structure Traversal Example:")
    nested_data = [1, [2, 3, [4, 5]], [6, [7, 8]]]
    print("Sum of nested data structure:", nested_sum(nested_data))

    print("*" * 80)

# Recursive function to calculate factorial
def factorial(n):
    """
    Calculates the factorial of a given number using recursion.
    Factorial of n (n!) is the product of all positive integers up to n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Recursive function to generate Fibonacci numbers
def fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursion.
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ... where Fib(n) = Fib(n-1) + Fib(n-2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive function to sum elements in a nested data structure
def nested_sum(data):
    """
    Calculates the sum of elements in a nested data structure (e.g., lists within lists)
    using recursion. Traverses each level, summing all integers within.
    """
    total = 0
    for element in data:
        if isinstance(element, list):
            total += nested_sum(element)  # Recursive call for nested lists
        else:
            total += element
    return total

if __name__ == "__main__":
    main()
