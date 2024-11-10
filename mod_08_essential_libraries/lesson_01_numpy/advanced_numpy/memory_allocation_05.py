#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Memory Allocation Numpy
#
# Description: This program explains how to understand and manage memory
#              allocation in NumPy. It demonstrates checking memory usage
#              and optimizing memory allocation for large datasets.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
    print("========== Understanding and Managing Memory Allocation in NumPy ==========")
    explain_memory_usage()
    explain_memory_optimization()
    demonstrate_float_size()

# Explains how to check memory usage of a NumPy array
def explain_memory_usage():
    # Creating a large NumPy array with one million elements
    array = np.arange(1000000)

    # Memory usage of the entire array in bytes
    print("\nMemory usage of the array in bytes:", array.nbytes)

    # Checking the memory size of a single element in the array
    print("Size of one element in bytes:", array.itemsize)

    # Total number of elements in the array
    print("Number of elements in the array:", array.size)

# Explains and demonstrates memory optimization techniques in NumPy
def explain_memory_optimization():
    # Example 1: Using smaller data types to save memory
    large_array = np.arange(1000000, dtype=np.int64)  # Using int64 (8 bytes per element)
    optimized_array = np.arange(1000000, dtype=np.int32)  # Using int32 (4 bytes per element)

    print("\nMemory usage of int64 array:", large_array.nbytes, "bytes")  # 8 MB
    print("Memory usage of int32 array:", optimized_array.nbytes, "bytes")  # 4 MB

    # Explanation: By using int32 instead of int64, we halve the memory usage.

    # Example 2: Using memory views to avoid copying data
    # Creating a view of the optimized array
    view_array = optimized_array.view()

    print("\nMemory view created. No additional memory allocation is done.")
    print("Memory usage of the view (same as the original):", view_array.nbytes, "bytes")

    # Explanation: Memory views share the same data buffer as the original array,
    # meaning no extra memory is used, and changes in one will reflect in the other.

# Demonstrates checking the size of float numbers in a NumPy array
def demonstrate_float_size():
    # Creating a float array with one million elements
    float_array = np.arange(1000000, dtype=np.float64)  # Using float64 (8 bytes per element)

    print("\nMemory usage of float64 array:", float_array.nbytes, "bytes")
    print("Size of one float element in bytes:", float_array.itemsize)

    # Using a smaller float type to save memory
    optimized_float_array = np.arange(1000000, dtype=np.float32)  # Using float32 (4 bytes per element)

    print("Memory usage of float32 array:", optimized_float_array.nbytes, "bytes")
    print("Size of one optimized float element in bytes:", optimized_float_array.itemsize)

if __name__ == "__main__":
    main()
