#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Rumpy Views And Copies
#
# Description: This program explains the difference between views and copies
#              in NumPy arrays. It shows how to create views and copies
#              and demonstrates how modifying them affects the original data.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Views and Copies in NumPy ==========")
    demonstrate_views()
    demonstrate_copies()

# Demonstrates creating a view of a NumPy array
def demonstrate_views():
    original_array = np.array([1, 2, 3, 4, 5])
    view_array = original_array[1:4]             # Creates a view of the original array

    print("\nOriginal Array:", original_array)
    print("View of the Array (elements 1 to 3):", view_array)

    # Modifying the view affects the original array
    view_array[0] = 99
    print("Modified View:", view_array)
    print("Original Array after modifying the view:", original_array)

# Demonstrates creating a copy of a NumPy array
def demonstrate_copies():
    original_array = np.array([1, 2, 3, 4, 5])
    copy_array = original_array.copy()           # Creates a copy of the original array

    print("\nOriginal Array:", original_array)
    print("Copy of the Array:", copy_array)

    # Modifying the copy does NOT affect the original array
    copy_array[0] = 99
    print("Modified Copy:", copy_array)
    print("Original Array after modifying the copy:", original_array)

if __name__ == "__main__":
    main()