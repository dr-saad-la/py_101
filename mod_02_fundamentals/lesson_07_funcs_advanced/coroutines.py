#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: coroutines_generators_yield
#
# Description: This program demonstrates the use of coroutines and
#              generators with `yield` and `yield from` in Python.
#              Coroutines allow for asynchronous programming, and `yield from`
#              simplifies nested generator delegation.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import asyncio

def main():
    print("========== Coroutines and Generators with yield and yield from ==========")
    print("This program demonstrates asynchronous programming and data streaming.")
    print("*" * 80)

    # Demonstrate generator with yield
    print("Simple generator example with yield:")
    for number in simple_generator(5):
        print(number)

    print("\nNested generator example with yield from:")
    for value in main_generator():
        print(value)

    # Demonstrate coroutine with asyncio
    print("\nAsynchronous coroutine example:")
    asyncio.run(async_coroutine_example())

    print("*" * 80)


# Simple generator function using yield
def simple_generator(n: int):
    """
    Generates numbers from 1 up to n using yield.

    Args:
        n (int): The upper limit of the range to generate.

    Yields:
        int: The next number in the range.
    """
    for i in range(1, n + 1):
        yield i


# Nested generator with yield from
def sub_generator():
    """
    A sub-generator that yields a sequence of values.
    """
    yield "Sub-generator value 1"
    yield "Sub-generator value 2"
    yield "Sub-generator value 3"

def main_generator():
    """
    Main generator that uses yield from to delegate to sub_generator.
    """
    yield "Main generator start"
    yield from sub_generator()
    yield "Main generator end"


# Asynchronous coroutine with yield
async def async_coroutine_example():
    """
    An example of an asynchronous coroutine that uses asyncio.sleep
    to mimic asynchronous behavior.
    """
    print("Starting asynchronous coroutine...")
    await asyncio.sleep(1)  # Simulate async delay
    print("Asynchronous coroutine resumed after delay.")
    await asyncio.sleep(1)  # Simulate async delay again
    print("Asynchronous coroutine completed.")

if __name__ == "__main__":
    main()
