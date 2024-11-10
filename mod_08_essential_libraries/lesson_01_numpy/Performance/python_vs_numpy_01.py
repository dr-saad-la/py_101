#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Vs Native Python
#
# Description: This program compares the performance of NumPy with native
#              Python in handling mathematical operations, demonstrating
#              the efficiency of NumPy.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np
import time

def main():
    print("========== NumPy vs. Native Python Performance Comparison ==========")
    compare_numpy_and_python()

# Demonstrates performance comparison between NumPy and native Python
def compare_numpy_and_python():
    # Creating a large list and array
    size = 10**6
    list1 = [i for i in range(size)]
    list2 = [i for i in range(size)]
    array1 = np.array(list1)
    array2 = np.array(list2)

    # Using native Python for element-wise addition
    start_time = time.time()
    result_list = [list1[i] + list2[i] for i in range(size)]
    python_duration = time.time() - start_time
    print(f"\nTime taken using native Python: {python_duration:.5f} seconds")

    # Using NumPy for element-wise addition
    start_time = time.time()
    result_array = array1 + array2
    numpy_duration = time.time() - start_time
    print(f"Time taken using NumPy: {numpy_duration:.5f} seconds")

    # Display the performance improvement
    improvement = python_duration / numpy_duration
    print(f"\nPerformance Improvement: {improvement:.2f} times faster with NumPy")

if __name__ == "__main__":
    main()