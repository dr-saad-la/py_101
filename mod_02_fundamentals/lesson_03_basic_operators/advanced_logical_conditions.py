#!/usr/bin/env python3

# =========================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Advanced Conditional Logic and Operators
#
# Description: This program demonstrates advanced concepts in conditional
#              logic and operators, including truthy/falsy values,
#              short-circuiting, bitwise operations, identity/equality,
#              ternary expressions, list comprehensions, XOR, and De Morgan's Laws.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =========================================================================

def main():
    print("=== Demonstrating Truthy and Falsy Values ===")
    truthy_falsy_values()

    print("\n=== Demonstrating Short-Circuiting ===")
    short_circuiting()

    print("\n=== Demonstrating Bitwise Shifts ===")
    bitwise_shifts()

    print("\n=== Compound Assignment Operators with Bitwise Operations ===")
    compound_bitwise_operations()

    print("\n=== Identity vs Equality ===")
    identity_vs_equality()

    print("\n=== Ternary (Conditional) Expressions ===")
    ternary_expressions()

    print("\n=== Conditional Expressions in List Comprehensions ===")
    list_comprehension_conditional()

    print("\n=== Bitwise XOR Example ===")
    bitwise_xor_example()

    print("\n=== Demonstrating De Morgan’s Laws ===")
    de_morgans_laws()

def truthy_falsy_values():
    values = [0, 1, "", "Non-empty string", [], [1, 2], None]
    for value in values:
        print(f"{value!r} is {'truthy' if bool(value) else 'falsy'}")

def short_circuiting():
    print("Evaluating True or False:")
    result = True or expensive_computation()
    print(f"Result of True or expensive_computation(): {result}")

    print("Evaluating False and True:")
    result = False and expensive_computation()
    print(f"Result of False and expensive_computation(): {result}")

def expensive_computation():
    print("This function was called.")
    return True

def bitwise_shifts():
    num = 4
    print(f"{num} << 1 (Left Shift): {num << 1}")
    print(f"{num} >> 1 (Right Shift): {num >> 1}")

def compound_bitwise_operations():
    a = 6  # binary: 110
    b = 3  # binary: 011
    print(f"Initial a: {a} (binary: {bin(a)})")
    a &= b
    print(f"a &= b: {a} (binary: {bin(a)})")
    a |= b
    print(f"a |= b: {a} (binary: {bin(a)})")
    a ^= b
    print(f"a ^= b: {a} (binary: {bin(a)})")

def identity_vs_equality():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"list1 == list2: {list1 == list2}")  # True, values are equal
    print(f"list1 is list2: {list1 is list2}")  # False, different objects in memory

def ternary_expressions():
    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"Age: {age}, Status: {status}")

def list_comprehension_conditional():
    numbers = [1, 2, 3, 4, 5, 6]
    even_squares = [n * n for n in numbers if n % 2 == 0]
    print(f"Even squares: {even_squares}")

def bitwise_xor_example():
    a = 10  # binary: 1010
    b = 12  # binary: 1100
    result = a ^ b
    print(f"Bitwise XOR of {a} and {b}: {result} (binary: {bin(result)})")

def de_morgans_laws():
    a, b = True, False
    print(f"not (a and b): {not (a and b)} == (not a or not b): {not a or not b}")
    print(f"not (a or b): {not (a or b)} == (not a and not b): {not a and not b}")

if __name__ == "__main__":
    main()
