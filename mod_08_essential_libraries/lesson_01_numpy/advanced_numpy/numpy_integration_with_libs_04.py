#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_with_pandas_matplotlib
#
# Description: This program demonstrates how to use NumPy in conjunction
#              with Pandas and Matplotlib for data analysis and visualization.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("========== Using NumPy with Pandas and Matplotlib ==========")
    demonstrate_numpy_with_pandas()
    demonstrate_numpy_with_matplotlib()

# Demonstrates using NumPy arrays with Pandas
def demonstrate_numpy_with_pandas():
    # Create a NumPy array
    data = np.array([10, 20, 30, 40, 50])

    # Create a Pandas DataFrame using the NumPy array
    df = pd.DataFrame(data, columns=["Values"])
    print("\nPandas DataFrame created from NumPy array:\n", df)

    # Perform operations on the DataFrame
    df["Doubled"] = df["Values"] * 2
    print("\nDataFrame after adding a 'Doubled' column:\n", df)

# Demonstrates using NumPy arrays with Matplotlib for plotting
def demonstrate_numpy_with_matplotlib():
    # Generate data using NumPy
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a simple plot
    plt.plot(x, y, label="sin(x)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Plot of sin(x) using Matplotlib")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()