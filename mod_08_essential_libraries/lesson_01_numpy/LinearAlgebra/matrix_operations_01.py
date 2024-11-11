#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Linear Algebra
#
# Description: This program demonstrates matrix and vector operations
#              using the NumPy library. It covers matrix multiplication,
#              addition, element-wise operations, transposition, and
#              vector operations.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Matrix and Vector Operations in NumPy ==========")
	demonstrate_matrix_multiplication()
	demonstrate_matrix_addition()
	demonstrate_elementwise_multiplication()
	demonstrate_matrix_transposition()
	demonstrate_vector_operations()


# Demonstrates how to multiply matrices using NumPy
def demonstrate_matrix_multiplication():
	matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
	matrix_b = np.array([[7, 8], [9, 10], [11, 12]])
	result = np.dot(matrix_a, matrix_b)
	
	print("\nMatrix A:\n", matrix_a)
	print("\nMatrix B:\n", matrix_b)
	print("\nResult of Matrix Multiplication (A x B):\n", result)


# Demonstrates matrix addition
def demonstrate_matrix_addition():
	matrix_a = np.array([[1, 2], [3, 4]])
	matrix_b = np.array([[5, 6], [7, 8]])
	result = np.add(matrix_a, matrix_b)
	
	print("\nMatrix A:\n", matrix_a)
	print("\nMatrix B:\n", matrix_b)
	print("\nResult of Matrix Addition (A + B):\n", result)


# Demonstrates element-wise multiplication
def demonstrate_elementwise_multiplication():
	matrix_a = np.array([[1, 2], [3, 4]])
	matrix_b = np.array([[5, 6], [7, 8]])
	result = np.multiply(matrix_a, matrix_b)
	
	print("\nMatrix A:\n", matrix_a)
	print("\nMatrix B:\n", matrix_b)
	print("\nResult of Element-wise Multiplication (A * B):\n", result)


# Demonstrates matrix transposition
def demonstrate_matrix_transposition():
	matrix = np.array([[1, 2, 3], [4, 5, 6]])
	transposed = np.transpose(matrix)
	
	print("\nOriginal Matrix:\n", matrix)
	print("\nTransposed Matrix:\n", transposed)


# Demonstrates vector operations
def demonstrate_vector_operations():
	vector_a = np.array([1, 2, 3])
	vector_b = np.array([4, 5, 6])
	
	dot_product = np.dot(vector_a, vector_b)
	cross_product = np.cross(vector_a, vector_b)
	
	print("\nVector A:", vector_a)
	print("\nVector B:", vector_b)
	print("\nDot Product (A . B):", dot_product)
	print("\nCross Product (A x B):", cross_product)


if __name__ == "__main__":
	main()