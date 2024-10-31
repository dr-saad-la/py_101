#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Nested For Loops
#
# Description: Demonstrates advanced usage of nested loops in Python
#              with applications in matrix processing, pattern generation,
#              and dynamic data structures.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import random


def main():
	
	print("============ Advanced Nested Loops in Python ============")
	print("Exploring nested loops and complex data structures.".center(80))
	print("Nested loops are loops within loops, allowing iteration over multi-dimensional data structures.")
	print("*" * 80)
	
	matrix_multiplication()
	print("-" * 80)
	dynamic_grid_generation()
	print("-" * 80)
	pattern_printing()
	print("-" * 80)
	conditional_nested_loop()
	print("*" * 80)


# Example 1: Matrix Multiplication Using Nested Loops
def matrix_multiplication():
	"""
	Demonstrates matrix multiplication using nested loops.
	"""
	print("Example 1: Matrix Multiplication with Nested Loops")
	
	# Define two 3x3 matrices
	matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
	
	# Initialize result matrix with zeros
	result = [[0 for _ in range(3)] for _ in range(3)]
	
	# Perform matrix multiplication
	for i in range(len(matrix_a)):
		for j in range(len(matrix_b[0])):
			for k in range(len(matrix_b)):
				result[i][j] += matrix_a[i][k] * matrix_b[k][j]
	
	# Print resulting matrix
	print("Result of Matrix Multiplication:")
	for row in result:
		print(row)
	print("Matrix multiplication completed.\n")


# Example 2: Dynamic Grid Generation with Nested Loops
def dynamic_grid_generation():
	"""
	Generates a 5x5 grid with random integers between 1 and 100.
	"""
	print("Example 2: Dynamic 5x5 Grid Generation with Random Integers")
	
	# Define grid size and initialize empty grid
	grid_size = 5
	grid = [[random.randint(1, 100) for _ in range(grid_size)] for _ in range(grid_size)]
	
	# Display the generated grid
	print("Generated Grid:")
	for row in grid:
		print(row)
	print("Grid generation completed.\n")


# Example 3: Pattern Printing with Nested Loops
def pattern_printing():
	"""
	Prints a triangle pattern using nested loops.
	"""
	print("Example 3: Pattern Printing (Triangle) Using Nested Loops")
	
	# Define pattern size
	n = 5
	
	# Generate triangle pattern
	for i in range(1, n + 1):
		for j in range(i):
			print("*", end=" ")
		print()
	print("Pattern printing completed.\n")


# Example 4: Conditional Nested Loop with Early Termination
def conditional_nested_loop():
	"""
	Demonstrates nested loops with early termination using break.
	"""
	print("Example 4: Nested Loops with Conditional Early Termination")
	
	# Loop with conditional break
	for i in range(1, 6):
		print(f"Outer Loop {i}:")
		for j in range(1, 6):
			if j > 3:  # Condition for early termination of the inner loop
				print("   Breaking inner loop at j =", j)
				break
			print(f"   Inner Loop {j}")
	print("Conditional nested loop completed.\n")


if __name__ == "__main__":
	main()