#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_broadcasting
#
# Description: This program explains broadcasting in NumPy. It covers
#              the rules of broadcasting, demonstrates operations between
#              arrays of different shapes, and lists practical use cases.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Understanding Broadcasting in NumPy ==========")
	explain_broadcasting_rules()
	demonstrate_basic_broadcasting()
	demonstrate_advanced_broadcasting()
	list_practical_use_cases()


# Explains the rules of broadcasting
def explain_broadcasting_rules():
	print("\nRules of Broadcasting:")
	print("1. If two arrays have different ranks, the shape of the smaller-rank array is padded with ones on the left side.")
	print("2. Arrays are compatible for broadcasting if their shapes are equal or one of them is 1 in the dimension.")
	print("3. Broadcasting occurs element-wise along dimensions.")


# Demonstrates the basic rules and operations with broadcasting
def demonstrate_basic_broadcasting():
	print("\nBasic Broadcasting Examples:")
	
	# Example 1: Adding a scalar to an array
	array = np.array([1, 2, 3])
	scalar = 5
	result = array + scalar
	print(f"Array: {array} + Scalar: {scalar} = {result}")
	
	# Example 2: Adding a 1D array to a 2D array
	array_2d = np.array([[1, 2, 3], [4, 5, 6]])
	array_1d = np.array([10, 20, 30])
	result = array_2d + array_1d
	print("\n2D Array:\n", array_2d)
	print("1D Array:", array_1d)
	print("Result of Broadcasting:\n", result)


# Demonstrates more complex broadcasting scenarios and rules
def demonstrate_advanced_broadcasting():
	print("\nAdvanced Broadcasting Examples:")
	
	# Example 1: Multiplying arrays with different shapes
	array_2d = np.array([[1, 2], [3, 4], [5, 6]])
	array_1d = np.array([10, 20])
	result = array_2d * array_1d
	print("\n2D Array:\n", array_2d)
	print("1D Array:", array_1d)
	print("Result of Broadcasting:\n", result)
	
	# Example 2: Subtracting a row vector from a matrix
	matrix = np.array([[1, 2, 3], [4, 5, 6]])
	row_vector = np.array([1, 1, 1])
	result = matrix - row_vector
	print("\nMatrix:\n", matrix)
	print("Row Vector:", row_vector)
	print("Result of Broadcasting:\n", result)


# Lists practical use cases of broadcasting
def list_practical_use_cases():
	print("\nPractical Use Cases of Broadcasting:")
	print("• Adding a constant to each element of an array.")
	print("• Scaling arrays of different shapes in matrix calculations.")


if __name__ == "__main__":
	main()