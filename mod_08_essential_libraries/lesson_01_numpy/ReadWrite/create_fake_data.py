import numpy as np

# Generate a 5x3 array of random integers between 1 and 100
fake_data = np.random.randint(1, 101, (5, 3))

# Save the random data to 'data.csv' using the savetxt function
np.savetxt("data.csv", fake_data, delimiter=",", fmt="%d")

print("Fake data generated and saved to data.csv:")
print(fake_data)