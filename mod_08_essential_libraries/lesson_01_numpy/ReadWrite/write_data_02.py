#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_saving_loading_arrays
#
# Description: This program demonstrates how to save and load NumPy arrays
#              using the `numpy.save()` and `numpy.load()` functions. It
#              includes examples of saving arrays to `.npy` files and
#              loading them back.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Saving and Loading Arrays ==========")
    demonstrate_saving_arrays()
    demonstrate_loading_arrays()

# Demonstrates saving arrays using `numpy.save()`
def demonstrate_saving_arrays():
    array = np.array([1, 2, 3, 4, 5])
    np.save("my_array.npy", array)  # Saves the array to a .npy file
    print("\nArray saved to 'my_array.npy'")

# Demonstrates loading arrays using `numpy.load()`
def demonstrate_loading_arrays():
    try:
        loaded_array = np.load("my_array.npy")  # Loads the array from the .npy file
        print("\nArray loaded from 'my_array.npy':", loaded_array)
    except FileNotFoundError:
        print("\nFile 'my_array.npy' not found. Please make sure the file exists in the directory.")

if __name__ == "__main__":
    main()