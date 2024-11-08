#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Array Indexing Slicing
#
# Description: This program demonstrates array indexing and slicing
#              techniques using the NumPy library.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Array Indexing and Slicing in NumPy ==========")
    demonstrate_basic_indexing()
    demonstrate_negative_indexing()
    demonstrate_slicing()
    demonstrate_step_slicing()
    demonstrate_2d_array_indexing()

# Demonstrates basic indexing of arrays
def demonstrate_basic_indexing():
    array = np.array([10, 20, 30, 40, 50])
    print("\nBasic Indexing:")
    print("Array:", array)
    print("First element:", array[0])
    print("Third element:", array[2])

# Demonstrates negative indexing of arrays
def demonstrate_negative_indexing():
    array = np.array([10, 20, 30, 40, 50])
    print("\nNegative Indexing:")
    print("Array:", array)
    print("Last element:", array[-1])
    print("Second to last element:", array[-2])

# Demonstrates slicing of arrays
def demonstrate_slicing():
    array = np.array([10, 20, 30, 40, 50, 60, 70])
    print("\nArray Slicing:")
    print("Array:", array)
    print("Elements from index 1 to 4:", array[1:5])  # Slices from index 1 to 4
    print("Elements from index 3 to the end:", array[3:])  # Slices from index 3 to the end
    print("Elements from the start to index 3:", array[:4])  # Slices from the start to index 3

# Demonstrates slicing with a step
def demonstrate_step_slicing():
    array = np.array([10, 20, 30, 40, 50, 60, 70])
    print("\nStep Slicing:")
    print("Array:", array)
    print("Every second element:", array[::2])  # Slices every second element
    print("Elements in reverse order:", array[::-1])  # Slices in reverse order

# Demonstrates indexing and slicing in a 2D array
def demonstrate_2d_array_indexing():
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\n2D Array Indexing and Slicing:")
    print("2D Array:\n", array_2d)
    print("Element at row 0, column 1:", array_2d[0, 1])  # Indexing specific element
    print("First row:", array_2d[0, :])  # Slicing the first row
    print("Second column:", array_2d[:, 1])  # Slicing the second column

if __name__ == "__main__":
    main()