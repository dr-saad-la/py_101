#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: arithmetic_ops_01
#
# Description: Demonstrates arithmetic operators in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    
    print("============ Printing the Arithmetic Operators =============")
    print_arithmetic_operators()
    print("*"*72)
    
    print("Perform Simple Arithmetic Operations".center(72))
    arithmetic_ops()
    print("*" * 72)


# Function to print arithmetic operators and their descriptions
def print_arithmetic_operators():
    """
    Print the arithmetic operators.
    """
    
    print("Arithmetic Operators in Python:")
    print("+ : Addition (adds two numbers)")
    print("- : Subtraction (subtracts second number from the first)")
    print("* : Multiplication (multiplies two numbers)")
    print("/ : Division (divides the first number by the second)")
    print("// : Floor Division (divides and returns the integer result)")
    print("% : Modulus (returns remainder when first number is divided by second)")
    print("** : Exponentiation (raises the first number to the power of the second)")

# Function to demonstrate arithmetic operations
def arithmetic_ops():
    a = 10
    b = 3
    print("\nArithmetic Operations Examples:")
    print(f"{a} + {b} = {a + b}")    # Addition
    print(f"{a} - {b} = {a - b}")    # Subtraction
    print(f"{a} * {b} = {a * b}")    # Multiplication
    print(f"{a} / {b} = {a / b}")    # Division
    print(f"{a} // {b} = {a // b}")  # Floor Division
    print(f"{a} % {b} = {a % b}")    # Modulus
    print(f"{a} ** {b} = {a ** b}")   # Exponentiation

if __name__ == "__main__":
    main()
