#pip install numpy
import numpy as np

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5])

# Basic arithmetic operations
added = a + 2  # Add 2 to each element
multiplied = a * 2  # Multiply each element by 2

# Statistical operations
mean_val = np.mean(a)  # Mean of the array
max_val = np.max(a)    # Maximum value in the array

# Display results
print("Original array:", a)
print("Added:", added)
print("Multiplied:", multiplied)
print("Mean:", mean_val)
print("Max:", max_val)
