#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: comparison_ops_02
#
# Description: Demonstrates comparison operators in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
def main():
    print("==== Print the Comparison Operators")
    print_comparison_operators()
    
    print("Perform Comparison Operators")
    comparison_ops()


# Function to print comparison operators and their descriptions
def print_comparison_operators():
    print("Comparison Operators in Python:")
    print("== : Equal to (checks if two values are equal)")
    print("!= : Not equal to (checks if two values are not equal)")
    print("<  : Less than (checks if the first value is less than the second)")
    print(">  : Greater than (checks if the first value is greater than the second)")
    print("<= : Less than or equal to (checks if the first value is less than or equal to the second)")
    print(">= : Greater than or equal to (checks if the first value is greater than or equal to the second)")

# Function to demonstrate comparison operations
def comparison_ops():
    x = 5
    y = 10
    print("\nComparison Operations Examples:")
    print(f"{x} == {y} -> {x == y}")   # Equal to
    print(f"{x} != {y} -> {x != y}")   # Not equal to
    print(f"{x} < {y} -> {x < y}")     # Less than
    print(f"{x} > {y} -> {x > y}")     # Greater than
    print(f"{x} <= {y} -> {x <= y}")   # Less than or equal to
    print(f"{x} >= {y} -> {x >= y}")   # Greater than or equal to


if __name__ == "__main__":
    main()