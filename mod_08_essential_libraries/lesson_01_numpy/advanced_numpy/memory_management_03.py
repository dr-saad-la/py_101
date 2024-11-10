#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_memory_management
#
# Description: This program provides insights into memory allocation and
#              efficient memory management in NumPy. It demonstrates how
#              to view memory usage and manage arrays efficiently.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Memory Management in NumPy ==========")
    demonstrate_memory_usage()
    demonstrate_memory_views()

# Demonstrates checking memory usage of an array
def demonstrate_memory_usage():
    array = np.arange(1000000, dtype=np.float64)  # Create a large array
    memory_usage = array.nbytes                   # Get memory usage in bytes
    print(f"\nMemory usage of the array: {memory_usage / (1024**2):.2f} MB")  # Convert to MB

# Demonstrates using views to save memory
def demonstrate_memory_views():
    original_array = np.arange(10)
    print("\nOriginal Array:", original_array)

    # Create a view of the original array
    view_array = original_array.view()
    view_array[0] = 99                           # Modify the view

    print("Modified View Array:", view_array)
    print("Original Array After Modification:", original_array)  # Original array also changes

    # Check if the arrays share the same memory
    print("\nDo the arrays share memory?", np.shares_memory(original_array, view_array))

if __name__ == "__main__":
    main()