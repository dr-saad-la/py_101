#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_statistical_functions
#
# Description: This program demonstrates various statistical functions
#              using NumPy, such as computing means, medians, and standard
#              deviations, as well as summarizing arrays with basic operations.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Statistical Functions in NumPy ==========")
	demonstrate_means_medians_std()
	demonstrate_summarizing_arrays()


# Demonstrates computing means, medians, and standard deviations
def demonstrate_means_medians_std():
	data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
	
	mean = np.mean(data)
	median = np.median(data)
	std_dev = np.std(data)
	
	print("\nData Array:", data)
	print("Mean of Data:", mean)
	print("Median of Data:", median)
	print("Standard Deviation of Data:", std_dev)


# Demonstrates summarizing arrays with sum(), min(), and max()
def demonstrate_summarizing_arrays():
	data = np.array([3, 5, 7, 2, 8, 10, 4, 1, 6, 9])
	
	total_sum = np.sum(data)
	minimum_value = np.min(data)
	maximum_value = np.max(data)
	
	print("\nData Array:", data)
	print("Sum of Data:", total_sum)
	print("Minimum Value in Data:", minimum_value)
	print("Maximum Value in Data:", maximum_value)


if __name__ == "__main__":
	main()