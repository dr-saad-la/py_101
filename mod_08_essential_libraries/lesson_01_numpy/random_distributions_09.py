#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Numpy Random Distributions Extended
#
# Description: This program illustrates how to generate arrays from
#              different random distributions using NumPy. Examples
#              include uniform, normal, binomial, Poisson, exponential,
#              chi-square, logistic, and beta distributions.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np

def main():
    print("========== Random Distributions in NumPy ==========")
    demonstrate_uniform_distribution()
    demonstrate_normal_distribution()
    demonstrate_binomial_distribution()
    demonstrate_poisson_distribution()
    demonstrate_random_integers()
    demonstrate_exponential_distribution()
    demonstrate_chisquare_distribution()
    demonstrate_logistic_distribution()
    demonstrate_beta_distribution()

# Demonstrates generating a uniform distribution
def demonstrate_uniform_distribution():
    print("\nGenerating an array with a uniform distribution:")
    uniform_array = np.random.uniform(0, 1, 10)  # 10 random numbers between 0 and 1
    print("Uniform Distribution Array:", uniform_array)

# Demonstrates generating a normal distribution
def demonstrate_normal_distribution():
    print("\nGenerating an array with a normal distribution:")
    normal_array = np.random.normal(0, 1, 10)  # Mean = 0, Std Dev = 1, 10 random numbers
    print("Normal Distribution Array:", normal_array)

# Demonstrates generating a binomial distribution
def demonstrate_binomial_distribution():
    print("\nGenerating an array with a binomial distribution:")
    binomial_array = np.random.binomial(10, 0.5, 10)  # 10 trials, 50% probability of success
    print("Binomial Distribution Array:", binomial_array)

# Demonstrates generating a Poisson distribution
def demonstrate_poisson_distribution():
    print("\nGenerating an array with a Poisson distribution:")
    poisson_array = np.random.poisson(5, 10)  # Lambda = 5, 10 random numbers
    print("Poisson Distribution Array:", poisson_array)

# Demonstrates generating random integers
def demonstrate_random_integers():
    print("\nGenerating an array of random integers:")
    random_integers_array = np.random.randint(1, 100, 10)  # 10 random integers between 1 and 100
    print("Random Integers Array:", random_integers_array)

# Demonstrates generating an exponential distribution
def demonstrate_exponential_distribution():
    print("\nGenerating an array with an exponential distribution:")
    exponential_array = np.random.exponential(1, 10)  # Scale = 1, 10 random numbers
    print("Exponential Distribution Array:", exponential_array)

# Demonstrates generating a chi-square distribution
def demonstrate_chisquare_distribution():
    print("\nGenerating an array with a chi-square distribution:")
    chisquare_array = np.random.chisquare(2, 10)  # Degrees of freedom = 2, 10 random numbers
    print("Chi-Square Distribution Array:", chisquare_array)

# Demonstrates generating a logistic distribution
def demonstrate_logistic_distribution():
    print("\nGenerating an array with a logistic distribution:")
    logistic_array = np.random.logistic(0, 1, 10)  # Mean = 0, Scale = 1, 10 random numbers
    print("Logistic Distribution Array:", logistic_array)

# Demonstrates generating a beta distribution
def demonstrate_beta_distribution():
    print("\nGenerating an array with a beta distribution:")
    beta_array = np.random.beta(2, 5, 10)  # Alpha = 2, Beta = 5, 10 random numbers
    print("Beta Distribution Array:", beta_array)

if __name__ == "__main__":
    main()