#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Time Series Analysis Numpy
#
# Description: This program demonstrates how to analyze time-series data
#              using NumPy. It covers generating sample time-series data,
#              calculating rolling averages, and detecting trends or
#              seasonality in the data.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import numpy as np


def main():
	print("========== Time-Series Data Analysis with NumPy ==========")
	generate_time_series_data()
	calculate_rolling_average()
	detect_trends()


# Generates sample time-series data
def generate_time_series_data():
	# Simulating daily temperature data over 10 days
	days = np.arange(1, 11)
	temperatures = np.array([30, 32, 31, 29, 35, 36, 33, 32, 30, 31])
	
	print("\nTime (days):", days)
	print("Temperatures (°C):", temperatures)


# Calculates the rolling average of the time-series data
def calculate_rolling_average():
	temperatures = np.array([30, 32, 31, 29, 35, 36, 33, 32, 30, 31])
	window_size = 3
	
	# Calculate rolling average using NumPy's convolution
	rolling_avg = np.convolve(temperatures, np.ones(window_size) / window_size, mode='valid')
	print("\nRolling average (3-day window):", rolling_avg)


# Detects simple trends in the time-series data
def detect_trends():
	temperatures = np.array([30, 32, 31, 29, 35, 36, 33, 32, 30, 31])
	trend = np.polyfit(np.arange(len(temperatures)), temperatures, 1)  # Linear trend
	trend_line = np.polyval(trend, np.arange(len(temperatures)))
	
	print("\nDetected trend line:", trend_line)
	print("Trend slope:", trend[0])  # The slope of the trend


if __name__ == "__main__":
	main()