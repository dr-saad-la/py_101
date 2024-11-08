#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Array Broadcasting
#
# Description: This program explains and demonstrates the concept of
#              broadcasting in NumPy, showing how operations between
#              arrays of different shapes can be efficiently handled.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Broadcasting in NumPy ==========")
	demonstrate_simple_broadcasting()
	demonstrate_row_vector_broadcasting()
	demonstrate_column_vector_broadcasting()
	demonstrate_broadcasting_with_scalars()
	demonstrate_incompatible_shapes()


# Example 1: Broadcasting a scalar to an array
def demonstrate_simple_broadcasting():
	array = np.array([1, 2, 3, 4])
	scalar = 5
	result = array + scalar  # The scalar is broadcasted to match the shape of the array
	print("\nArray:", array, "with shape", array.shape)
	print("Scalar:", scalar)
	print("Result of adding scalar to array:", result)


# Example 2: Broadcasting a row vector across a 2D array
def demonstrate_row_vector_broadcasting():
	matrix = np.array([[1, 2, 3], [4, 5, 6]])
	row_vector = np.array([10, 20, 30])
	result = matrix + row_vector  # The row vector is broadcasted to each row of the matrix
	print("\nMatrix:\n", matrix, "with shape", matrix.shape)
	print("Row Vector:", row_vector, "with shape", row_vector.shape)
	print("Result of adding row vector to matrix:\n", result)


# Example 3: Broadcasting a column vector across a 2D array
def demonstrate_column_vector_broadcasting():
	matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	column_vector = np.array([[10], [20], [30]])
	result = matrix + column_vector  # The column vector is broadcasted to each column of the matrix
	print("\nMatrix:\n", matrix, "with shape", matrix.shape)
	print("Column Vector:\n", column_vector, "with shape", column_vector.shape)
	print("Result of adding column vector to matrix:\n", result)


# Example 4: Broadcasting with scalars
def demonstrate_broadcasting_with_scalars():
	array = np.arange(6).reshape(2, 3)
	print("\nArray:\n", array)
	
	# Scalar operations (broadcasting the scalar to all elements)
	print("Array + 10:\n", array + 10)
	print("Array * 2:\n", array * 2)


# Example 5: Handling incompatible shapes
def demonstrate_incompatible_shapes():
	array1 = np.array([1, 2, 3])
	array2 = np.array([[1, 2], [3, 4], [5, 6]])  # Incompatible shapes for broadcasting
	try:
		result = array1 + array2
	except ValueError as e:
		print("\nAttempting to broadcast arrays with incompatible shapes:")
		print("Array 1:", array1)
		print("Array 2:\n", array2)
		print("Error:", e)


if __name__ == "__main__":
	main()