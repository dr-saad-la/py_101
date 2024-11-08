#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Data Types Conversion
#
# Description: This program explores data types in NumPy arrays and how to
#              convert between different data types. It demonstrates
#              creating arrays with specific data types and converting
#              array types using NumPy methods.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Data Types and Type Conversion in NumPy ==========")
	demonstrate_array_data_types()
	demonstrate_type_conversion()


# Demonstrates creating arrays with specific data types
def demonstrate_array_data_types():
	# Integer array
	int_array = np.array([1, 2, 3, 4], dtype=np.int32)
	print("\nInteger Array:", int_array)
	print("Data type of int_array:", int_array.dtype)
	
	# Float array
	float_array = np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float64)
	print("\nFloat Array:", float_array)
	print("Data type of float_array:", float_array.dtype)
	
	# Boolean array
	bool_array = np.array([1, 0, 1, 0], dtype=np.bool_)
	print("\nBoolean Array:", bool_array)
	print("Data type of bool_array:", bool_array.dtype)
	
	# Complex number array
	complex_array = np.array([1 + 2j, 3 + 4j], dtype=np.complex_)
	print("\nComplex Number Array:", complex_array)
	print("Data type of complex_array:", complex_array.dtype)


# Demonstrates type conversion (casting) in NumPy arrays
def demonstrate_type_conversion():
	# Original integer array
	int_array = np.array([10, 20, 30, 40])
	print("\nOriginal Integer Array:", int_array)
	
	# Convert integer array to float
	float_array = int_array.astype(np.float64)
	print("Converted to Float Array:", float_array)
	print("Data type of float_array:", float_array.dtype)
	
	# Convert float array to integer
	float_array = np.array([10.5, 20.7, 30.9, 40.1])
	int_converted_array = float_array.astype(np.int32)
	print("\nOriginal Float Array:", float_array)
	print("Converted to Integer Array:", int_converted_array)
	print("Data type of int_converted_array:", int_converted_array.dtype)
	
	# Convert integer array to boolean
	bool_converted_array = int_array.astype(np.bool_)
	print("\nInteger Array Converted to Boolean Array:", bool_converted_array)
	print("Data type of bool_converted_array:", bool_converted_array.dtype)


if __name__ == "__main__":
	main()