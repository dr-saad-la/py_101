import numpy as np

# Generate a 5x3 array of random integers between 1 and 100
fake_data = np.random.randint(1, 101, (5, 3))

# Save the random data to 'data.csv' using the savetxt function
np.savetxt("data.csv", fake_data, delimiter=",", fmt="%d")

print("Fake data generated and saved to data.csv:")
print(fake_data)

# Generate a 5x3 array of random integers between 1 and 100
random_data = np.random.randint(1, 101, (5, 3)).astype(float)

# Introduce missing values (NaN) in the array
random_data[1, 2] = np.nan  # Example: Set one value to NaN
random_data[3, 0] = np.nan  # Example: Set another value to NaN

# Save the data with missing values to 'data_with_missing.csv'
np.savetxt("data_with_missing.csv", random_data, delimiter=",", fmt="%.2f")

print("Data with missing values generated and saved to data_with_missing.csv:")
print(random_data)