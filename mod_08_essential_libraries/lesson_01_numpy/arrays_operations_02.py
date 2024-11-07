#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_advanced
#
# Description: This program demonstrates advanced NumPy features,
#              including array slicing, reshaping, broadcasting,
#              and working with mathematical and statistical functions.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
    print("========== Advanced Features in NumPy ==========")
    demonstrate_array_slicing()
    demonstrate_array_reshaping()
    demonstrate_broadcasting()
    demonstrate_mathematical_functions()
    demonstrate_statistical_functions()


# Demonstrates array slicing and indexing
def demonstrate_array_slicing():
    print("\nArray slicing and indexing:")
    array = np.array([10, 20, 30, 40, 50, 60, 70])

    print("Original array:", array)
    print("First element:", array[0])  # Access first element
    print("Last element:", array[-1])  # Access last element
    print("Elements from index 2 to 5:", array[2:6])  # Slicing
    print("Elements with step of 2:", array[::2])  # Slicing with step


# Demonstrates reshaping arrays
def demonstrate_array_reshaping():
    print("\nArray reshaping:")
    array = np.arange(1, 13)  # Array with elements from 1 to 12
    reshaped_array = array.reshape(3, 4)  # Reshape into 3x4 array

    print("Original array:", array)
    print("Reshaped to 3x4 array:\n", reshaped_array)


# Demonstrates broadcasting
def demonstrate_broadcasting():
    print("\nBroadcasting example:")
    array_1 = np.array([1, 2, 3])
    array_2 = np.array([[10], [20], [30]])

    result = array_1 + array_2  # Broadcasting adds array_1 to each row of array_2
    print("Array 1:", array_1)
    print("Array 2:\n", array_2)
    print("Result of broadcasting:\n", result)


# Demonstrates mathematical functions
def demonstrate_mathematical_functions():
    print("\nMathematical functions:")
    array = np.array([1, 4, 9, 16, 25])

    print("Original array:", array)
    print("Square root of each element:", np.sqrt(array))
    print("Exponential (e^x) of each element:", np.exp(array))
    print("Logarithm (base 10) of each element:", np.log10(array))


# Demonstrates statistical functions
def demonstrate_statistical_functions():
    print("\nStatistical functions:")
    array = np.array([[1, 2, 3], [4, 5, 6]])

    print("Original array:\n", array)
    print("Mean of all elements:", np.mean(array))
    print("Median of all elements:", np.median(array))
    print("Standard deviation:", np.std(array))
    print("Variance:", np.var(array))
    print("Maximum element:", np.max(array))
    print("Minimum element:", np.min(array))
    print("Sum of elements along axis 0:", np.sum(array, axis=0))
    print("Sum of elements along axis 1:", np.sum(array, axis=1))


if __name__ == "__main__":
    main()
