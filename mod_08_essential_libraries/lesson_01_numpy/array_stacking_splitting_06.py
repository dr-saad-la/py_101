#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_array_stacking_splitting
#
# Description: This program demonstrates stacking and splitting arrays
#              using the NumPy library. It includes horizontal stacking,
#              vertical stacking, and splitting arrays into subarrays.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Array Stacking and Splitting in NumPy ==========")
	demonstrate_horizontal_stacking()
	demonstrate_vertical_stacking()
	demonstrate_array_splitting()


# Demonstrates horizontal stacking of arrays
def demonstrate_horizontal_stacking():
	array1 = np.array([1, 2, 3])
	array2 = np.array([4, 5, 6])
	print("\nArray 1:", array1)
	print("Array 2:", array2)
	
	# Horizontal stacking
	stacked_array = np.hstack((array1, array2))
	print("Horizontally Stacked Array:", stacked_array)


# Demonstrates vertical stacking of arrays
def demonstrate_vertical_stacking():
	array1 = np.array([[1, 2, 3]])
	array2 = np.array([[4, 5, 6]])
	print("\nArray 1:\n", array1)
	print("Array 2:\n", array2)
	
	# Vertical stacking
	stacked_array = np.vstack((array1, array2))
	print("Vertically Stacked Array:\n", stacked_array)


# Demonstrates splitting an array into subarrays
def demonstrate_array_splitting():
	array = np.arange(12).reshape(3, 4)  # Creates a 3x4 array
	print("\nOriginal Array:\n", array)
	
	# Splitting the array into two subarrays along columns
	split_array = np.hsplit(array, 2)
	print("Horizontally Split Arrays:")
	for subarray in split_array:
		print(subarray)
	
	# Splitting the array into three subarrays along rows
	split_array = np.vsplit(array, 3)
	print("\nVertically Split Arrays:")
	for subarray in split_array:
		print(subarray)


if __name__ == "__main__":
	main()