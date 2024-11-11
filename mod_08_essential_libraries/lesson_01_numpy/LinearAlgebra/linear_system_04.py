#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Solving Linear Systems with NumPy
#
# Description: This program demonstrates how to solve systems of linear
#              equations using the NumPy library. It provides a clear
#              explanation of using the np.linalg.solve() function to
#              find solutions efficiently.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Solving Systems of Linear Equations with NumPy ==========")
    solve_linear_system()

# Function to solve a system of linear equations using np.linalg.solve()
def solve_linear_system():
    # Define the coefficient matrix (A) and the right-hand side vector (b)
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])

    # Check if the matrix is singular (not invertible)
    if np.linalg.det(A) == 0:
        print("\nError: The coefficient matrix (A) is singular and does not have a unique solution.")
    else:
        # Solve the system of equations Ax = b
        x = np.linalg.solve(A, b)
        print("\nCoefficient Matrix (A):\n", A)
        print("\nRight-hand Side Vector (b):\n", b)
        print("\nSolution (x):\n", x)

if __name__ == "__main__":
    main()