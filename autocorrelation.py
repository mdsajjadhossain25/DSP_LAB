import numpy as np

# Define the sequence x(n)
x = np.array([1, 3, 5, 7])

# Length of the sequence
N = len(x)

# Array to store the autocorrelation values
# The range of autocorrelation values goes from -N+1 to N-1
autocorrelation = np.zeros(2 * N - 1)

# Calculate autocorrelation
for m in range(-N + 1, N):
    r_m = 0  # This will store the summation result for r_x(m)
    for n in range(N):
        if 0 <= n - m < N:  # Ensure indices are within bounds
            r_m += x[n] * x[n - m]  # Accumulate x(n) * x(n - m)
    autocorrelation[m + N - 1] = r_m  # Store the result in the array

# Display the autocorrelation result with indices
print("Autocorrelation r_x(m):")
for i, value in enumerate(autocorrelation):
    lag = i - (N - 1)  # Calculate the lag value for each index
    print(f"r_x({lag}) = {value}")
