#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Linear Algebra: QR Decomposition, SVD, Cholesky Decomposition
#
# Description: This program demonstrates how to perform QR Decomposition,
#              Singular Value Decomposition (SVD), and Cholesky Decomposition
#              using the NumPy library.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== QR Decomposition, SVD, and Cholesky Decomposition in NumPy ==========")
    demonstrate_qr_decomposition()
    demonstrate_svd()
    demonstrate_cholesky_decomposition()

# Demonstrates QR Decomposition of a matrix
def demonstrate_qr_decomposition():
    # Define a 2x2 matrix
    matrix = np.array([[12, -51], [6, 167]])

    # Perform QR Decomposition using np.linalg.qr()
    Q, R = np.linalg.qr(matrix)
    print("\nMatrix:\n", matrix)
    print("\nOrthogonal Matrix Q:\n", Q)
    print("\nUpper Triangular Matrix R:\n", R)

# Demonstrates Singular Value Decomposition (SVD) of a matrix
def demonstrate_svd():
    # Define a 2x3 matrix
    matrix = np.array([[1, 2, 3], [4, 5, 6]])

    # Perform Singular Value Decomposition using np.linalg.svd()
    U, S, Vt = np.linalg.svd(matrix)
    print("\nMatrix:\n", matrix)
    print("\nU Matrix (Left Singular Vectors):\n", U)
    print("\nSingular Values:\n", S)
    print("\nVt Matrix (Right Singular Vectors):\n", Vt)

# Demonstrates Cholesky Decomposition of a matrix
def demonstrate_cholesky_decomposition():
    # Define a positive-definite 2x2 matrix
    matrix = np.array([[4, 2], [2, 3]])

    try:
        # Perform Cholesky Decomposition using np.linalg.cholesky()
        L = np.linalg.cholesky(matrix)
        print("\nMatrix:\n", matrix)
        print("\nCholesky Decomposition (Lower Triangular Matrix L):\n", L)
    except np.linalg.LinAlgError:
        print("\nMatrix:\n", matrix)
        print("The matrix is not positive-definite and cannot be decomposed using Cholesky Decomposition.")

if __name__ == "__main__":
    main()