#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Mathematical Functions
#
# Description: This program showcases the use of various mathematical
#              functions available in the NumPy library, including basic
#              arithmetic, trigonometric, logarithmic, and other advanced
#              functions.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Mathematical Functions in NumPy ==========")
	demonstrate_basic_arithmetic()
	demonstrate_trigonometric_functions()
	demonstrate_exponential_and_logarithmic_functions()
	demonstrate_aggregate_functions()


# Demonstrates basic arithmetic functions
def demonstrate_basic_arithmetic():
	array = np.array([1, 2, 3, 4, 5])
	print("\nOriginal Array:", array)
	print("Square Root of Array:", np.sqrt(array))
	print("Exponential of Array:", np.exp(array))
	print("Natural Log of Array:", np.log(array))
	print("Log Base 10 of Array:", np.log10(array))
	print("Array Squared:", np.square(array))


# Demonstrates trigonometric functions
def demonstrate_trigonometric_functions():
	angles = np.array([0, np.pi / 2, np.pi, 3 * np.pi / 2])
	print("\nAngles (in radians):", angles)
	print("Sine of Angles:", np.sin(angles))
	print("Cosine of Angles:", np.cos(angles))
	print("Tangent of Angles:", np.tan(angles))
	
	# Inverse trigonometric functions
	values = np.array([1, -1, 0])
	print("\nValues for Inverse Trigonometric Functions:", values)
	print("Arcsine of Values:", np.arcsin(values))
	print("Arccosine of Values:", np.arccos(values))
	print("Arctangent of Values:", np.arctan(values))


# Demonstrates exponential and logarithmic functions
def demonstrate_exponential_and_logarithmic_functions():
	array = np.array([1, 2, 3, 10])
	print("\nOriginal Array for Exponential and Logarithmic Functions:", array)
	print("Exponential (e^x):", np.exp(array))
	print("Exponential (2^x):", np.exp2(array))
	print("Natural Logarithm:", np.log(array))
	print("Log Base 10:", np.log10(array))
	print("Log Base 2:", np.log2(array))


# Demonstrates aggregate functions
def demonstrate_aggregate_functions():
	array = np.array([1, 2, 3, 4, 5])
	print("\nArray for Aggregate Functions:", array)
	print("Sum of Array Elements:", np.sum(array))
	print("Product of Array Elements:", np.prod(array))
	print("Mean of Array:", np.mean(array))
	print("Median of Array:", np.median(array))
	print("Standard Deviation of Array:", np.std(array))
	print("Variance of Array:", np.var(array))
	print("Maximum Value in Array:", np.max(array))
	print("Minimum Value in Array:", np.min(array))


if __name__ == "__main__":
	main()