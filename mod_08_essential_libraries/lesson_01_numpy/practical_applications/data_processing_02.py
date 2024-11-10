#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Data Preprocessing Numpy
#
# Description: This program demonstrates how to use NumPy for data preprocessing
#              tasks, such as handling missing values, normalizing data, and
#              filtering data based on specific conditions.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Data Preprocessing with NumPy ==========")
	handle_missing_values()
	normalize_data()
	filter_data()


# Handles missing values in a dataset
def handle_missing_values():
	data = np.array([10, np.nan, 25, 30, np.nan, 45])
	print("\nOriginal data with missing values:", data)
	
	# Replace missing values with the mean of the non-missing values
	mean_value = np.nanmean(data)
	data = np.where(np.isnan(data), mean_value, data)
	print("Data after handling missing values:", data)


# Normalizes data to have a mean of 0 and a standard deviation of 1
def normalize_data():
	data = np.array([50, 60, 70, 80, 90])
	print("\nOriginal data:", data)
	
	# Calculate mean and standard deviation
	mean = np.mean(data)
	std_dev = np.std(data)
	
	# Normalize the data
	normalized_data = (data - mean) / std_dev
	print("Normalized data:", normalized_data)


# Filters data based on a specific condition
def filter_data():
	data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	print("\nOriginal data:", data)
	
	# Filter data to keep only values greater than 5
	filtered_data = data[data > 5]
	print("Filtered data (values > 5):", filtered_data)


if __name__ == "__main__":
	main()