#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Numpy Linear Algebra Functionality
#
# Description: This program provides an overview of the `numpy.linalg`
#              module, demonstrating various linear algebra functions
#              such as matrix operations, solving equations, eigenvalues,
#              matrix rank, and more.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Using numpy.linalg Module ==========")
    demonstrate_linalg_functions()

# Demonstrates the use of various functions in numpy.linalg
def demonstrate_linalg_functions():
    # Example matrix and vector
    A = np.array([[2, -1], [4, 3]])
    B = np.array([[1, 2], [3, 4]])
    b = np.array([1, 7])

    # 1. Calculate the determinant
    determinant = np.linalg.det(A)
    print("\n1. Determinant of Matrix A:", determinant)

    # 2. Calculate the inverse
    if determinant != 0:
        inverse = np.linalg.inv(A)
        print("\n2. Inverse of Matrix A:\n", inverse)
    else:
        print("\n2. Matrix A is singular and does not have an inverse.")

    # 3. Solve the system of equations Ax = b
    try:
        solution = np.linalg.solve(A, b)
        print("\n3. Solution to Ax = b:", solution)
    except np.linalg.LinAlgError:
        print("\n3. Matrix A is singular; no unique solution exists.")

    # 4. Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("\n4. Eigenvalues of Matrix A:", eigenvalues)
    print("   Eigenvectors of Matrix A:\n", eigenvectors)

    # 5. Calculate the matrix rank
    rank = np.linalg.matrix_rank(A)
    print("\n5. Rank of Matrix A:", rank)

    # 6. Compute the trace (sum of diagonal elements)
    trace = np.trace(A)
    print("\n6. Trace of Matrix A:", trace)

    # 7. Norm of a matrix
    norm = np.linalg.norm(A)
    print("\n7. Norm of Matrix A:", norm)

    # 8. QR decomposition
    Q, R = np.linalg.qr(A)
    print("\n8. QR Decomposition of Matrix A:")
    print("   Q Matrix:\n", Q)
    print("   R Matrix:\n", R)

    # 9. Singular Value Decomposition (SVD)
    U, S, Vt = np.linalg.svd(A)
    print("\n9. Singular Value Decomposition (SVD) of Matrix A:")
    print("   U Matrix:\n", U)
    print("   Singular Values:", S)
    print("   Vt Matrix:\n", Vt)

    # 10. Cholesky decomposition (only if the matrix is positive-definite)
    try:
        cholesky_decomp = np.linalg.cholesky(B)
        print("\n10. Cholesky Decomposition of Matrix B:\n", cholesky_decomp)
    except np.linalg.LinAlgError:
        print("\n10. Matrix B is not positive-definite; Cholesky decomposition failed.")

if __name__ == "__main__":
    main()