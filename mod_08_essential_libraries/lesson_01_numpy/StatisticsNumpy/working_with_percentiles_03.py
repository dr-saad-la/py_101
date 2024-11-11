#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_percentiles_quantiles
#
# Description: This program demonstrates how to compute percentiles and
#              quantiles using NumPy. These functions are useful for
#              summarizing data distributions.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Percentiles and Quantiles in NumPy ==========")
    demonstrate_percentiles_quantiles()

# Demonstrates computing percentiles and quantiles
def demonstrate_percentiles_quantiles():
    # Generate some random data
    data = np.random.randint(1, 100, 50)  # Random integers between 1 and 100

    print("\nData Sample (first 10 values):", data[:10])

    # Compute and display the 25th, 50th, and 75th percentiles
    percentile_25 = np.percentile(data, 25)
    percentile_50 = np.percentile(data, 50)
    percentile_75 = np.percentile(data, 75)

    print("25th Percentile:", percentile_25)
    print("50th Percentile (Median):", percentile_50)
    print("75th Percentile:", percentile_75)

    # Compute and display quantiles (0.25, 0.5, 0.75 quantiles)
    quantile_25 = np.quantile(data, 0.25)
    quantile_50 = np.quantile(data, 0.5)
    quantile_75 = np.quantile(data, 0.75)

    print("0.25 Quantile:", quantile_25)
    print("0.5 Quantile (Median):", quantile_50)
    print("0.75 Quantile:", quantile_75)

if __name__ == "__main__":
    main()