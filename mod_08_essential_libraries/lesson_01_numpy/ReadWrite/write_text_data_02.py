#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Writing Data with NumPy (Text Files)
#
# Description: This program demonstrates how to write data to text files
#              using NumPy's savetxt() function. It shows how to format
#              and save arrays in a CSV format for easy data handling.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Writing Data to Text File with NumPy ==========")
    demonstrate_savetxt()

# Demonstrates writing data to a text file using savetxt()
def demonstrate_savetxt():
    # Create a 2D array of random integers
    data = np.random.randint(1, 101, (5, 3))
    print("\nData to be written to text file:\n", data)

    # Write the array to a CSV file
    np.savetxt("output_data.csv", data, delimiter=",", fmt="%d")
    print("Data written to output_data.csv successfully!")

if __name__ == "__main__":
    main()
