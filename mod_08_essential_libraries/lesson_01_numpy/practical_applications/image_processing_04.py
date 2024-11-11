#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: image_processing_numpy
#
# Description: This program introduces basic image processing techniques
#              using NumPy. It demonstrates loading images as arrays,
#              converting images to grayscale, and applying simple filters.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

IMAGE_PATH = Path(r"../../../_assets/landscape.png").resolve()
OUTPUT_PATH = Path(r"../../../_assets").resolve()


def main():
	print("========== Basic Image Processing with NumPy ==========")
	load_and_display_image()
	convert_to_grayscale()
	apply_simple_filter()


# Load an image and display it
def load_and_display_image():
	image = Image.open(IMAGE_PATH)              # Load an image from a file
	image_array = np.array(image)                       # Convert image to a NumPy array
	print("\nOriginal Image Shape:", image_array.shape)
	
	plt.imshow(image_array)
	plt.title("Original Image")
	plt.axis("off")
	plt.show()


# Convert the image to grayscale
def convert_to_grayscale():
	image = Image.open(IMAGE_PATH).convert("L")  # Convert to grayscale
	grayscale_array = np.array(image)
	print("\nGrayscale Image Shape:", grayscale_array.shape)
	
	plt.imshow(grayscale_array, cmap="gray")
	plt.title("Grayscale Image")
	plt.axis("off")
	plt.show()


# Apply a simple edge-detection filter
def apply_simple_filter():
	image = Image.open(IMAGE_PATH).convert("L")
	image_array = np.array(image)
	
	# Define a simple edge-detection filter
	kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
	
	# Apply the filter using convolution
	filtered_image = np.zeros_like(image_array)
	for i in range(1, image_array.shape[0] - 1):
		for j in range(1, image_array.shape[1] - 1):
			sub_matrix = image_array[i - 1:i + 2, j - 1:j + 2]
			filtered_image[i, j] = np.sum(sub_matrix * kernel)
	
	# Clip the values to be in the range [0, 255]
	filtered_image = np.clip(filtered_image, 0, 255)
	print("\nFiltered Image Shape:", filtered_image.shape)
	
	plt.imshow(filtered_image, cmap="gray")
	plt.title("Filtered Image (Edge Detection)")
	plt.axis("off")
	plt.show()


if __name__ == "__main__":
	main()