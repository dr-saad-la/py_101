#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Creating Numpy Arrays
#
# Description: This program introduces the basics of creating arrays
#              using the NumPy library.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
import random
import numpy as np


def main():
    print("========== Array Creation with NumPy ==========")
    create_array_from_list()
    
    line_separator()
    create_array_from_tuple()
    
    line_separator()
    create_array_from_range()
    
    line_separator()
    create_array_of_zeros()
    
    line_separator()
    create_array_of_ones()
    
    line_separator()
    create_array_with_linspace()
    
    line_separator()
    create_array_of_random_integers()

# Creates an array from a list
def create_array_from_list():
    array_from_list = np.array([10, 20, 30, 40, 50])
    arr_from_random_list = np.array(generate_random_list(21, 6))
    print("Array from list:", array_from_list)
    print(f"Array from a random list: {arr_from_random_list}")

# Generate random data using Random
def generate_random_list(npop, nelem, seed=0):
    """
    Generate a random list of integers.
    """
    random.seed(seed)
    return list(random.choices(range(npop), k = nelem))

# Creates an array from a tuple
def create_array_from_tuple():
    array_from_tuple = np.array((1, 2, 3, 4))
    print("Array from tuple:", array_from_tuple)

# Creates an array from a range
def create_array_from_range():
    array_from_range = np.arange(0, 10, 2)
    print("Array from range:", array_from_range)

# Creates a 3x3 array of zeros
def create_array_of_zeros():
    array_zeros = np.zeros((3, 3))
    print("3x3 Array of zeros:\n", array_zeros)

# Creates a 2x4 array of ones
def create_array_of_ones():
    array_ones = np.ones((2, 4))
    print("2x4 Array of ones:\n", array_ones)

# Creates an array with evenly spaced values between 0 and 1
def create_array_with_linspace():
    array_linspace = np.linspace(0, 1, 5)
    print("Array with 5 evenly spaced values between 0 and 1:", array_linspace)

# Creates a 2x3 array of random integers between 1 and 100
def create_array_of_random_integers():
    array_random_integers = np.random.randint(1, 100, size=(2, 3))
    print("2x3 Array of random integers between 1 and 100:\n", array_random_integers)
    
    
def line_separator(nchar=72, char="*"):
    print(char * nchar)
    
if __name__ == "__main__":
    main()
