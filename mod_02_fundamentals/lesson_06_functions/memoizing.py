#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: function_caching_memoization
#
# Description: This program demonstrates function caching (memoization) in Python
#              using `functools.lru_cache`. Memoization is a technique for storing
#              the results of expensive function calls to improve performance when
#              the function is called with the same inputs again. This is especially
#              useful for recursive functions like Fibonacci series calculations.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

from functools import lru_cache

def main():
    print("========== Function Caching with Memoization in Python ==========")
    print("This program uses `lru_cache` to speed up Fibonacci calculations.")
    print("*" * 80)

    # Display Fibonacci series for a few values
    for i in range(11):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

    print("*" * 80)

    # Show caching statistics
    print("Cache info:")
    print(fibonacci.cache_info())
    print("*" * 80)

# Fibonacci function with memoization
@lru_cache(maxsize=None)  # No limit on cache size
def fibonacci(n):
    """
    Returns the nth Fibonacci number, using memoization to cache results.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    main()
