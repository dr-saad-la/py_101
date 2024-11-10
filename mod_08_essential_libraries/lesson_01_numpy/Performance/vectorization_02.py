#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Performance Optimization
#
# Description: This program demonstrates how to optimize performance in
#              NumPy by using vectorized operations instead of loops.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np
import time


def main():
    print("========== Performance Optimization with NumPy ==========")
    demonstrate_vectorized_operations()

# Demonstrates the speed advantage of vectorized operations in NumPy
def demonstrate_vectorized_operations():
    # Creating large arrays for the demonstration
    size = 10**6
    array1 = np.random.rand(size)
    array2 = np.random.rand(size)

    # Using a loop to add elements one-by-one
    start_time = time.time()
    result_loop = [array1[i] + array2[i] for i in range(size)]
    loop_duration = time.time() - start_time
    print(f"\nTime taken using loop: {loop_duration:.5f} seconds")

    # Using vectorized addition with NumPy
    start_time = time.time()
    result_vectorized = array1 + array2
    vectorized_duration = time.time() - start_time
    print(f"Time taken using vectorized operation: {vectorized_duration:.5f} seconds")

    # Display the performance improvement
    improvement = loop_duration / vectorized_duration
    print(f"\nPerformance Improvement: {improvement:.2f} times faster")

if __name__ == "__main__":
    main()