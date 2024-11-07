#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_introduction
#
# Description: This program provides an introduction to the NumPy library,
#              which is fundamental for scientific computing in Python.
#              It demonstrates creating arrays, basic array operations,
#              and how to use essential functions provided by NumPy.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Introduction to NumPy ==========")
	demonstrate_array_creation()
	demonstrate_array_operations()
	demonstrate_array_properties()


# Demonstrates creating arrays using NumPy
def demonstrate_array_creation():
	print("\nCreating arrays with NumPy:")
	array_1d = np.array([1, 2, 3, 4, 5])  # 1D array
	array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
	array_zeros = np.zeros((3, 3))  # 3x3 array of zeros
	array_ones = np.ones((2, 4))  # 2x4 array of ones
	array_range = np.arange(0, 10, 2)  # Array from 0 to 10 with step 2
	
	print("1D Array:", array_1d)
	print("2D Array:\n", array_2d)
	print("3x3 Array of Zeros:\n", array_zeros)
	print("2x4 Array of Ones:\n", array_ones)
	print("Array with range 0 to 10 (step 2):", array_range)


# Demonstrates basic array operations
def demonstrate_array_operations():
	print("\nPerforming basic array operations:")
	a = np.array([10, 20, 30, 40])
	b = np.array([1, 2, 3, 4])
	
	# Element-wise operations
	print("Addition:", a + b)
	print("Subtraction:", a - b)
	print("Multiplication:", a * b)
	print("Division:", a / b)
	
	# Array-wise operations
	print("Dot Product:", np.dot(a, b))  # Dot product of a and b
	print("Sum of all elements in 'a':", np.sum(a))
	print("Mean of elements in 'a':", np.mean(a))


# Demonstrates array properties
def demonstrate_array_properties():
	print("\nExploring array properties:")
	array = np.array([[1, 2, 3], [4, 5, 6]])
	
	print("Array:\n", array)
	print("Shape of the array:", array.shape)  # Shape of the array
	print("Number of dimensions:", array.ndim)  # Number of dimensions
	print("Data type of elements:", array.dtype)  # Data type of elements
	print("Size (number of elements):", array.size)  # Total number of elements


if __name__ == "__main__":
	main()