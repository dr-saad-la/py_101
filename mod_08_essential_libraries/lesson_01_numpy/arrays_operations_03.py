#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Array Operations
#
# Description: This program demonstrates various array operations
#              using the NumPy library.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Array Operations in NumPy ==========")
    demonstrate_addition()
    demonstrate_subtraction()
    demonstrate_multiplication()
    demonstrate_division()
    demonstrate_dot_product()
    demonstrate_sum_mean()

# Demonstrates element-wise addition
def demonstrate_addition():
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    print("\nAddition (element-wise):", a + b)

# Demonstrates element-wise subtraction
def demonstrate_subtraction():
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    print("\nSubtraction (element-wise):", a - b)

# Demonstrates element-wise multiplication
def demonstrate_multiplication():
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    print("\nMultiplication (element-wise):", a * b)

# Demonstrates element-wise division
def demonstrate_division():
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    print("\nDivision (element-wise):", a / b)

# Demonstrates dot product of two arrays
def demonstrate_dot_product():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("\nDot Product:", np.dot(a, b))  # Dot product calculation

# Demonstrates sum and mean of elements in an array
def demonstrate_sum_mean():
    a = np.array([10, 20, 30, 40])
    print("\nSum of elements in 'a':", np.sum(a))
    print("Mean of elements in 'a':", np.mean(a))

if __name__ == "__main__":
    main()