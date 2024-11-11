#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_histograms
#
# Description: This program demonstrates how to generate histograms using
#              NumPy to analyze the distribution of data.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np
import matplotlib.pyplot as plt

def main():
    print("========== Generating Histograms in NumPy ==========")
    generate_histogram()

# Demonstrates generating a histogram using NumPy and Matplotlib
def generate_histogram():
    # Generate some random data
    data = np.random.normal(50, 15, 1000)  # Mean: 50, Std Dev: 15, Sample Size: 1000

    print("\nData Sample (first 10 values):", data[:10])
    print("Generating histogram...")

    # Create a histogram
    plt.hist(data, bins=20, color='blue', alpha=0.7, edgecolor='black')
    plt.title("Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(axis='y', alpha=0.75)
    plt.show()

if __name__ == "__main__":
    main()