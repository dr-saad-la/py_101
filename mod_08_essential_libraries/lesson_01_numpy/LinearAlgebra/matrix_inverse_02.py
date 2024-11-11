#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Linalg Module
#
# Description: This program provides an introduction to the numpy.linalg
#              module, demonstrating basic linear algebra operations such
#              as calculating the determinant, inverse, and transpose of
#              matrices. It also covers basic matrix properties and checks
#              for singularity using condition number.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Using numpy.linalg Module (Basic Operations) ==========")
    demonstrate_determinant()
    demonstrate_inverse()
    demonstrate_transpose()
    check_singularity()

# Demonstrates calculating the determinant of a matrix
def demonstrate_determinant():
    matrix = np.array([[3, 2], [1, 4]])
    determinant = np.linalg.det(matrix)
    print("\nMatrix:\n", matrix)
    print("Determinant of the matrix:", determinant)

# Demonstrates calculating the inverse of a matrix with a determinant check
def demonstrate_inverse():
    matrix = np.array([[4, 7], [2, 6]])
    if np.linalg.det(matrix) != 0:  # Check if the matrix is invertible
        inverse_matrix = np.linalg.inv(matrix)
        print("\nMatrix:\n", matrix)
        print("Inverse of the matrix:\n", inverse_matrix)
    else:
        print("\nMatrix:\n", matrix)
        print("The matrix is not invertible (determinant is 0).")

# Demonstrates transposing a matrix
def demonstrate_transpose():
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    transposed_matrix = np.transpose(matrix)
    print("\nMatrix:\n", matrix)
    print("Transposed Matrix:\n", transposed_matrix)

# Checks for singularity using the condition number
def check_singularity():
    matrix = np.array([[4, 7], [2, 6]], dtype=np.float64)  # Use a specific floating-point data type
    condition_number = np.linalg.cond(matrix)
    
    # Compare the condition number with the inverse of machine epsilon
    if condition_number < 1 / np.finfo(np.float64).eps:
        print("\nMatrix:\n", matrix)
        print("The matrix is well-conditioned (condition number is reasonable).")
    else:
        print("\nMatrix:\n", matrix)
        print("The matrix is singular or nearly singular (condition number is large).")


if __name__ == "__main__":
    main()