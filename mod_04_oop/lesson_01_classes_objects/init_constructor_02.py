#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: The init method constructor
#
# Description: This program demonstrates the use of the `__init__()`
#              method, or constructor, in Python. The program creates
#              a `Student` class, allowing each instance to initialize
#              unique attributes using the constructor.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Understanding the `__init__()` Method (Constructor) in Python ==========")
    print("This program demonstrates the use of constructors for initializing objects with unique attributes.")
    print("*" * 80)

    # Create instances of the Student class
    student1 = Student("Alice", "Mathematics", 3.9)
    student2 = Student("Bob", "Physics", 3.5)

    # Display information for each student instance
    student1.display_info()
    student2.display_info()

    print("*" * 80)


# Define the Student class with an `__init__()` constructor
class Student:
    def __init__(self, name, major, gpa):
        """
        Initialize a new Student instance with name, major, and GPA attributes.

        Args:
            name (str): The student's name.
            major (str): The student's major field of study.
            gpa (float): The student's grade point average.
        """
        self.name = name  # Student's name
        self.major = major  # Major field of study
        self.gpa = gpa  # Grade point average

    def display_info(self):
        """
        Display information about the student in a readable format.
        """
        print(f"Student: {self.name}, Major: {self.major}, GPA: {self.gpa}")


if __name__ == "__main__":
    main()
