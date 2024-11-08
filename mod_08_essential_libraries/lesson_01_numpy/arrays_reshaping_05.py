#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Array Reshaping
#
# Description: This program demonstrates array reshaping techniques
#              using the NumPy library. Arrays are created using the
#              arange() method and then reshaped into different dimensions.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Array Reshaping in NumPy ==========")
    demonstrate_1d_to_2d_reshaping()
    demonstrate_reshaping_to_3d()
    demonstrate_flattening_array()
    demonstrate_transposing_array()
    demonstrate_resizing_array()


# Demonstrates reshaping a 1D array to a 2D array
def demonstrate_1d_to_2d_reshaping():
    array_1d = np.arange(12)  # Creates an array with values from 0 to 11
    print("\n1D Array:", array_1d)
    array_2d = array_1d.reshape(3, 4)  # Reshapes to a 3x4 2D array
    print("Reshaped to 2D (3x4):\n", array_2d)

# Demonstrates reshaping an array to 3D
def demonstrate_reshaping_to_3d():
    array_1d = np.arange(24)  # Creates an array with values from 0 to 23
    print("\n1D Array:", array_1d)
    array_3d = array_1d.reshape(2, 3, 4)  # Reshapes to a 2x3x4 3D array
    print("Reshaped to 3D (2x3x4):\n", array_3d)

# Demonstrates flattening a 2D array back to 1D
def demonstrate_flattening_array():
    array_2d = np.arange(12).reshape(3, 4)  # Creates and reshapes to a 3x4 2D array
    print("\n2D Array (3x4):\n", array_2d)
    array_flattened = array_2d.flatten()  # Flattens to a 1D array
    print("Flattened to 1D:", array_flattened)

# Demonstrates transposing a 2D array
def demonstrate_transposing_array():
    array_2d = np.arange(12).reshape(3, 4)  # Creates and reshapes to a 3x4 2D array
    print("\n2D Array (3x4):\n", array_2d)
    array_transposed = array_2d.T  # Transposes the array
    print("Transposed Array (4x3):\n", array_transposed)
    
# Demonstrates resizing an array
def demonstrate_resizing_array():
    array_1d = np.arange(8)  # Creates an array with values from 0 to 7
    print("\nOriginal 1D Array:", array_1d)
    array_resized = np.resize(array_1d, (3, 3))  # Resizes to a 3x3 array
    print("Resized to 3x3 Array:\n", array_resized)

if __name__ == "__main__":
    main()