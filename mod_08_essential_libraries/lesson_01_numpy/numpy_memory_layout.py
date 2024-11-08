#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Memory Layout
#
# Description: This program explains memory layout in NumPy arrays,
#              specifically C-order (row-major) and F-order (column-major).
#              It demonstrates creating arrays with different memory layouts
#              and how to check and change the memory layout.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Memory Layout in NumPy: C-order and F-order ==========")
	demonstrate_c_order_memory_layout()
	demonstrate_f_order_memory_layout()
	demonstrate_memory_layout_conversion()


# Demonstrates C-order (row-major) memory layout
def demonstrate_c_order_memory_layout():
	array_c = np.array([[1, 2, 3], [4, 5, 6]], order='C')  # Default is C-order
	print("\nC-order (Row-major) Array:\n", array_c)
	print("Memory layout (C-order):", array_c.flags['C_CONTIGUOUS'])


# Demonstrates F-order (column-major) memory layout
def demonstrate_f_order_memory_layout():
	array_f = np.array([[1, 2, 3], [4, 5, 6]], order='F')  # F-order specified
	print("\nF-order (Column-major) Array:\n", array_f)
	print("Memory layout (F-order):", array_f.flags['F_CONTIGUOUS'])


# Demonstrates how to convert between C-order and F-order
def demonstrate_memory_layout_conversion():
	array = np.array([[1, 2, 3], [4, 5, 6]], order='C')
	print("\nOriginal Array (C-order):\n", array)
	print("Is C-contiguous:", array.flags['C_CONTIGUOUS'])
	
	# Convert to F-order (column-major)
	array_f = np.asfortranarray(array)
	print("\nConverted to F-order (Column-major):\n", array_f)
	print("Is F-contiguous:", array_f.flags['F_CONTIGUOUS'])


if __name__ == "__main__":
	main()