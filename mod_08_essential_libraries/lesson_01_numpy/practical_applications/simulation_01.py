#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numerical Simulations Numpy
#
# Description: This program demonstrates how to use NumPy for multiple
#              numerical simulations, including random walks, normal
#              distribution sampling, and Monte Carlo simulations.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Numerical Simulations with NumPy ==========")
    simulate_random_walk()
    simulate_normal_distribution()
    monte_carlo_simulation()

# Simulates a simple random walk
def simulate_random_walk():
    np.random.seed(0)                                         # Set seed for reproducibility
    steps = 1000
    random_steps = np.random.choice([-1, 1], size=steps)   # Randomly choose -1 or 1
    random_walk = np.cumsum(random_steps)                     # Cumulative sum to simulate the walk

    print("\nSimulating a random walk:")
    print("First 10 steps:", random_walk[:10])
    print("Final position:", random_walk[-1])

# Simulates data from a normal distribution
def simulate_normal_distribution():
    np.random.seed(1)  # Set seed for reproducibility
    mean = 0
    std_dev = 1
    samples = 10000
    normal_data = np.random.normal(mean, std_dev, samples)  # Generate samples

    print("\nSimulating a normal distribution:")
    print("First 10 samples:", normal_data[:10])
    print("Mean of samples:", np.mean(normal_data))
    print("Standard deviation of samples:", np.std(normal_data))

# Performs a Monte Carlo simulation to estimate the value of π
def monte_carlo_simulation():
    np.random.seed(2)               # Set seed for reproducibility
    num_points = 1000000
    x = np.random.rand(num_points)  # Generate random x-coordinates
    y = np.random.rand(num_points)  # Generate random y-coordinates

    # Count the number of points that fall within the unit circle
    points_inside_circle = np.sum(x**2 + y**2 <= 1)
    pi_estimate = (points_inside_circle / num_points) * 4

    print("\nMonte Carlo simulation to estimate π:")
    print("Estimated value of π:", pi_estimate)

if __name__ == "__main__":
    main()