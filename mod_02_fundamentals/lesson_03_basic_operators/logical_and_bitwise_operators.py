#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: logical_and_bitwise_operators
#
# Description: This program demonstrates the use of logical operators `and`,
#              `or`, and bitwise operators `&` and `|`. It provides examples
#              of each possible combination with `True` and `False` values.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Logical and Bitwise Operators in Python ==========")
    print("This program demonstrates logical and bitwise operations with `True` and `False`.")
    print("*" * 80)

    # Logical AND and OR operators
    logical_operations()
    print("*" * 80)

    # Bitwise AND and OR operators
    bitwise_operations()
    print("*" * 80)


def logical_operations():
    """
    Demonstrates all possible combinations of `True` and `False` with
    logical `and` and `or` operators.
    """
    print("Logical Operators (and, or):")

    # `and` operator
    print("True and True:", True and True)      # Expected: True
    print("True and False:", True and False)    # Expected: False
    print("False and True:", False and True)    # Expected: False
    print("False and False:", False and False)  # Expected: False

    # `or` operator
    print("True or True:", True or True)        # Expected: True
    print("True or False:", True or False)      # Expected: True
    print("False or True:", False or True)      # Expected: True
    print("False or False:", False or False)    # Expected: False


def bitwise_operations():
    """
    Demonstrates all possible combinations of `True` and `False` with
    bitwise `&` and `|` operators.
    """
    print("Bitwise Operators (&, |):")

    # `&` operator (bitwise AND)
    print("True & True:", True & True)          # Expected: 1 (True)
    print("True & False:", True & False)        # Expected: 0 (False)
    print("False & True:", False & True)        # Expected: 0 (False)
    print("False & False:", False & False)      # Expected: 0 (False)

    # `|` operator (bitwise OR)
    print("True | True:", True | True)          # Expected: 1 (True)
    print("True | False:", True | False)        # Expected: 1 (True)
    print("False | True:", False | True)        # Expected: 1 (True)
    print("False | False:", False | False)      # Expected: 0 (False)


if __name__ == "__main__":
    main()
