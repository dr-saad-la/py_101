#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Array Properties
#
# Description: This program demonstrates the properties of arrays
#              using the NumPy library.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Array Properties in NumPy ==========")
    demonstrate_array_shape()
    demonstrate_array_dimensions()
    demonstrate_array_dtype()
    demonstrate_array_size()

# Demonstrates the shape of an array
def demonstrate_array_shape():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nArray:\n", array)
    print("Shape of the array:", array.shape)  # Shape of the array

# Demonstrates the number of dimensions of an array
def demonstrate_array_dimensions():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nNumber of dimensions:", array.ndim)  # Number of dimensions

# Demonstrates the data type of array elements
def demonstrate_array_dtype():
    array = np.array([1.5, 2.5, 3.5])
    print("\nData type of elements:", array.dtype)  # Data type of elements

# Demonstrates the total number of elements in an array
def demonstrate_array_size():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nSize (number of elements):", array.size)  # Total number of elements

if __name__ == "__main__":
    main()