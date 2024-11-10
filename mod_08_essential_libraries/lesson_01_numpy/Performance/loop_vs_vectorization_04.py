#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_efficient_operations
#
# Description: This program demonstrates how to avoid loops and use efficient
#              array operations in NumPy to optimize performance. By leveraging
#              vectorized operations, you can significantly speed up your code.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import time
import numpy as np

def main():
    print("========== Efficient Array Operations in NumPy ==========")
    demonstrate_loop_vs_vectorized()

# Demonstrates the performance difference between using loops and vectorized operations
def demonstrate_loop_vs_vectorized():
    # Creating a large array for demonstration
    array = np.random.rand(10**6)

    # Using a loop to calculate the square of each element
    start_time = time.time()
    squares_with_loop = [x**2 for x in array]  # Using a Python list comprehension
    end_time = time.time()
    loop_duration = end_time - start_time
    print(f"Time taken with loop: {loop_duration:.4f} seconds")

    # Using a vectorized operation to calculate the square of each element
    start_time = time.time()
    squares_with_vectorized = array**2  # Using NumPy's vectorized operation
    end_time = time.time()
    vectorized_duration = end_time - start_time
    print(f"Time taken with vectorized operation: {vectorized_duration:.4f} seconds")

    # Comparison
    print("\nUsing vectorized operations in NumPy is much faster than using loops in Python.")

if __name__ == "__main__":
    main()