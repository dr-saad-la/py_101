#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Rumpy Array Transpose Swapaxes
#
# Description: This program demonstrates how to transpose arrays and swap
#              axes using the NumPy library. It includes examples of
#              transposing 2D and 3D arrays and swapping axes.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Array Transposing and Swapping Axes in NumPy ==========")
	demonstrate_2d_array_transpose()
	demonstrate_3d_array_transpose()
	demonstrate_swap_axes()


# Demonstrates transposing a 2D array
def demonstrate_2d_array_transpose():
	array_2d = np.array([[1, 2, 3], [4, 5, 6]])
	print("\nOriginal 2D Array:\n", array_2d)
	
	# Transposing the 2D array
	transposed_array = array_2d.T
	print("Transposed 2D Array:\n", transposed_array)


# Demonstrates transposing a 3D array
def demonstrate_3d_array_transpose():
	array_3d = np.arange(24).reshape(2, 3, 4)
	print("\nOriginal 3D Array (2x3x4):\n", array_3d)
	
	# Transposing the 3D array: Change the order of axes
	transposed_array = array_3d.transpose(1, 0, 2)
	print("Transposed 3D Array (3x2x4):\n", transposed_array)


# Demonstrates swapping axes of an array
def demonstrate_swap_axes():
	array_3d = np.arange(24).reshape(2, 3, 4)
	print("\nOriginal 3D Array (2x3x4):\n", array_3d)
	
	# Swapping axes: Swap the first and second axes
	swapped_array = np.swapaxes(array_3d, 0, 1)
	print("Array After Swapping Axes (3x2x4):\n", swapped_array)


if __name__ == "__main__":
	main()