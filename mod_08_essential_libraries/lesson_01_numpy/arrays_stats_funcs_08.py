#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Statistical Functions
#
# Description: This program illustrates the use of various statistical
#              functions available in the NumPy library, including functions
#              for calculating mean, median, standard deviation, variance,
#              percentiles, and more.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Statistical Functions in NumPy ==========")
    demonstrate_central_tendency()
    demonstrate_dispersion_measures()
    demonstrate_percentiles_and_quantiles()
    demonstrate_statistical_summary()

# Demonstrates measures of central tendency
def demonstrate_central_tendency():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("\nData for Central Tendency Measures:", data)
    print("Mean of Data:", np.mean(data))
    print("Median of Data:", np.median(data))
    print("Mode of Data (using scipy): Note that NumPy does not have a built-in mode function.")

# Demonstrates measures of dispersion
def demonstrate_dispersion_measures():
    data = np.array([1, 2, 2, 3, 3, 4, 5, 5, 6])
    print("\nData for Dispersion Measures:", data)
    print("Standard Deviation of Data:", np.std(data))
    print("Variance of Data:", np.var(data))
    print("Range of Data:", np.ptp(data))  # Peak-to-peak range (max - min)

# Demonstrates percentiles and quantiles
def demonstrate_percentiles_and_quantiles():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("\nData for Percentiles and Quantiles:", data)
    print("25th Percentile:", np.percentile(data, 25))
    print("50th Percentile (Median):", np.percentile(data, 50))
    print("75th Percentile:", np.percentile(data, 75))
    print("Quantiles (0.25, 0.5, 0.75):", np.quantile(data, [0.25, 0.5, 0.75]))

# Demonstrates a statistical summary of the data
def demonstrate_statistical_summary():
    data = np.random.randint(1, 101, size=20)  # Generate 20 random integers between 1 and 100
    print("\nRandom Data for Statistical Summary:", data)
    print("Minimum Value:", np.min(data))
    print("Maximum Value:", np.max(data))
    print("Sum of All Values:", np.sum(data))
    print("Mean Value:", np.mean(data))
    print("Standard Deviation:", np.std(data))
    print("Variance:", np.var(data))
    print("25th, 50th, 75th Percentiles:", np.percentile(data, [25, 50, 75]))

if __name__ == "__main__":
    main()