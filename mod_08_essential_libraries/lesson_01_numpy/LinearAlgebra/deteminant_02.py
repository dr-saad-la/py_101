#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Linear Algebra: Determinant
#
# Description: This program demonstrates how to calculate the determinant
#              and inverse of a matrix using the NumPy library.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Determinant and Inverse of Matrices in NumPy ==========")
    demonstrate_determinant_and_inverse()

# Demonstrates how to calculate the determinant and inverse of a matrix
def demonstrate_determinant_and_inverse():
    # Define a 2x2 matrix
    matrix = np.array([[4, 7], [2, 6]])

    # Calculate the determinant using np.linalg.det()
    determinant = np.linalg.det(matrix)
    print("\nMatrix:\n", matrix)
    print("\nDeterminant of the matrix:", determinant)

    # Calculate the inverse using np.linalg.inv()
    if determinant != 0:  # Check if the matrix is invertible
        inverse = np.linalg.inv(matrix)
        print("\nInverse of the matrix:\n", inverse)
    else:
        print("\nThe matrix is not invertible.")

if __name__ == "__main__":
    main()