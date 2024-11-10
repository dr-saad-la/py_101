#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: numpy_structured_arrays
#
# Description: This program demonstrates how to create and use structured
#              arrays and record arrays in NumPy. It shows how to define
#              a custom data structure and access the data efficiently.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
    print("========== Structured and Record Arrays in NumPy ==========")
    demonstrate_structured_arrays()

# Demonstrates creating and using structured arrays
def demonstrate_structured_arrays():
    # Define a structured data type
    data_type = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]

    # Create a structured array
    people = np.array([
        ('Alice', 25, 5.5),
        ('Bob', 30, 6.0),
        ('Charlie', 35, 5.8)
    ], dtype=data_type)

    print("\nStructured Array:\n", people)

    # Access data using field names
    print("\nNames:", people['name'])
    print("Ages:", people['age'])
    print("Heights:", people['height'])

    # Modify data in the structured array
    people['age'][0] = 26                           # Update Alice's age
    print("\nUpdated Structured Array:\n", people)

if __name__ == "__main__":
    main()