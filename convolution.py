import numpy as np

# Define the sequences x(n) and h(n)
x = np.array([1, 2, 4])
h = np.array([1, 1, 1, 1, 1])

# Calculate the length of the output y(n) which is len(x) + len(h) - 1
output_length = len(x) + len(h) - 1
y = np.zeros(output_length)

# Perform the convolution using the summation formula explicitly
for n in range(output_length):
    y_n = 0  # This will store the summation result for y(n)
    for k in range(len(x)):
        if 0 <= n - k < len(h):  # Ensure indices are within bounds of h
            y_n += x[k] * h[n - k]  # Accumulate x(k) * h(n - k)
    y[n] = y_n  # Assign the computed value to y(n)

print("The convolution sum y(n) is:", y)
