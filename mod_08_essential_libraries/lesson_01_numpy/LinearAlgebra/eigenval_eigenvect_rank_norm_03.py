#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Numpy Linear Algebra: Eigenvalues, Eigenvectors, Matrix Rank, Norm
#
# Description: This program demonstrates how to calculate the eigenvalues,
#              eigenvectors, rank, and norm of a matrix using the NumPy library.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Eigenvalues, Eigenvectors, Rank, and Norm in NumPy ==========")
    demonstrate_eigenvalues_and_eigenvectors()
    demonstrate_rank()
    demonstrate_norm()

# Demonstrates how to calculate the eigenvalues and eigenvectors of a matrix
def demonstrate_eigenvalues_and_eigenvectors():
    # Define a 2x2 matrix
    matrix = np.array([[4, -2], [1, 1]])

    # Calculate the eigenvalues and eigenvectors using np.linalg.eig()
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    print("\nMatrix:\n", matrix)
    print("\nEigenvalues:", eigenvalues)
    print("\nEigenvectors:\n", eigenvectors)

# Demonstrates calculating the rank of a matrix
def demonstrate_rank():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rank = np.linalg.matrix_rank(matrix)
    print("\nMatrix:\n", matrix)
    print("Rank of the matrix:", rank)

# Demonstrates calculating the norm of a matrix
def demonstrate_norm():
    matrix = np.array([[1, 2], [3, 4]])
    norm = np.linalg.norm(matrix)
    print("\nMatrix:\n", matrix)
    print("Norm of the matrix:", norm)

if __name__ == "__main__":
    main()