#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: data_types
#
# Description: A demonstration of Python's key built-in data types, including
# numeric types, text types, and boolean types.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("Demonstrating Numeric Data Types")
    demonstrate_numeric_types()
    
    demonstrate_text_types()
    demonstrate_boolean_type()


def demonstrate_numeric_types() -> None:
    """
    Demonstrates Python's numeric types: int, float, and complex.
    """
    # Integer type: Whole numbers without decimal points
    count = 100
    print(f"Integer Example - Count: {count} (Type: {type(count)})")

    # Floating-point type: Numbers with decimal points
    temperature = 36.6
    print(f"Float Example - Temperature: {temperature}°C (Type: {type(temperature)})")

    # Complex number type: Numbers with real and imaginary parts
    complex_number = 3 + 4j
    print(f"Complex Example - Complex Number: {complex_number} (Type: {type(complex_number)})")
    print(f"  Real Part: {complex_number.real}, Imaginary Part: {complex_number.imag}\n")


def demonstrate_text_types() -> None:
    """
    Demonstrates Python's text type: str.
    """
    # String type: Textual data enclosed in quotes
    course_title = "Python Essentials"
    print(f"String Example - Greeting: {course_title} (Type: {type(course_title)})")

    # Multi-line string: Enclosed in triple quotes
    multi_line_text: str = """This is a
    multi-line string that spans
    several lines."""
    print(f"Multi-Line String Example:\n{multi_line_text}")
    print(f"Type of multi_line_text: {type(multi_line_text)}\n")


def demonstrate_boolean_type() -> None:
    """
    Demonstrates Python's boolean type: bool.
    """
    # Boolean type: Represents True or False values
    is_valid = True
    is_greater = 5 > 3

    print(f"Boolean Example - Is Valid: {is_valid} (Type: {type(is_valid)})")
    print(f"Comparison Example - Is 5 greater than 3? {is_greater} (Type: {type(is_greater)})\n")


if __name__ == "__main__":
    main()
