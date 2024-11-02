#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Instance Vs. Class Attributes
#
# Description: This program demonstrates the difference between instance and
#              class attributes in Python. It defines a `Car` class where
#              `make` and `model` are instance attributes specific to each car,
#              while `wheels` is a class attribute shared by all car instances.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Instance Attributes vs Class Attributes in Python ==========")
    print("This program demonstrates how instance attributes differ from class attributes.")
    print("*" * 80)

    # Create instances of the Car class
    car1 = Car("Toyota", "Corolla")
    car2 = Car("Ford", "Mustang")

    # Display information for each car instance
    car1.display_info()
    car2.display_info()

    # Show that the class attribute is shared across instances
    print("\nClass attribute `wheels` (shared by all cars):", Car.wheels)

    print("*" * 80)

# Define the Car class with class and instance attributes
class Car:
    # Class attribute, shared by all instances
    wheels = 4

    def __init__(self, make, model):
        """
        Initialize a new Car instance with make and model as instance attributes.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
        """
        self.make = make  # Instance attribute unique to each car
        self.model = model  # Instance attribute unique to each car

    def display_info(self):
        """
        Display information about the car, including its make, model, and wheels.
        """
        print(f"Car: {self.make} {self.model}, Wheels: {Car.wheels}")


if __name__ == "__main__":
    main()
