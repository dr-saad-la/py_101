#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Reading Writing Data
#
# Description: This program demonstrates how to read data from text files
#              and CSVs using NumPy. It includes examples of reading CSV
#              files using `numpy.loadtxt()` and `numpy.genfromtxt()`.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Reading Data from Text Files and CSVs ==========")
	demonstrate_reading_with_loadtxt()
	demonstrate_reading_with_genfromtxt()


# Demonstrates reading data from a text file using `numpy.loadtxt()`
def demonstrate_reading_with_loadtxt():
	# Example: Reading a CSV file (data.csv should be present in the same directory)
	try:
		data = np.loadtxt("data.csv", delimiter=",")
		print("\nData read using loadtxt():\n", data)
	except FileNotFoundError:
		print("\nFile data.csv not found. Please make sure the file exists in the directory.")


# Demonstrates reading data from a text file using `numpy.genfromtxt()`
def demonstrate_reading_with_genfromtxt():
	# Example: Reading a CSV file with missing values
	try:
		data = np.genfromtxt("data_with_missing.csv", delimiter=",", filling_values=0)
		print("\nData read using genfromtxt() (with missing values filled):\n", data)
	except FileNotFoundError:
		print("\nFile data_with_missing.csv not found. Please make sure the file exists in the directory.")


if __name__ == "__main__":
	main()
