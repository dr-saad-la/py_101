#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_memory_efficient_types
#
# Description: This program demonstrates how to use memory-efficient data
#              types in NumPy to optimize performance, particularly when
#              working with large datasets.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Memory-Efficient Data Types in NumPy ==========")
    demonstrate_memory_efficient_types()

# Demonstrates the use of memory-efficient data types
def demonstrate_memory_efficient_types():
    # Creating arrays with different data types
    array_float64 = np.ones(10**6, dtype=np.float64)  # Default data type (64-bit)
    array_float32 = np.ones(10**6, dtype=np.float32)  # More memory-efficient (32-bit)
    array_int32 = np.ones(10**6, dtype=np.int32)      # 32-bit integer
    array_int16 = np.ones(10**6, dtype=np.int16)      # 16-bit integer

    # Calculating memory usage
    memory_float64 = array_float64.nbytes
    memory_float32 = array_float32.nbytes
    memory_int32 = array_int32.nbytes
    memory_int16 = array_int16.nbytes

    print(f"Memory usage of float64 array: {memory_float64 / (1024**2):.2f} MB")
    print(f"Memory usage of float32 array: {memory_float32 / (1024**2):.2f} MB")
    print(f"Memory usage of int32 array: {memory_int32 / (1024**2):.2f} MB")
    print(f"Memory usage of int16 array: {memory_int16 / (1024**2):.2f} MB")

    # Performance impact (example)
    print("\nUsing memory-efficient data types can reduce memory usage significantly without sacrificing much performance.")

if __name__ == "__main__":
    main()