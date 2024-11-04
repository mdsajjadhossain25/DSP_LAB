import numpy as np
import matplotlib.pyplot as plt

# Signal parameters remain the same
Fs = 8000             # Sampling frequency in Hz
T = 1 / Fs            # Sampling period
N = 8                 # Number of points for the DFT
n = np.arange(N)      # Sample index

# Frequencies in the signal
f1 = 1000             # Frequency of first sine wave in Hz
f2 = 2000             # Frequency of second sine wave in Hz

# Calculate x(n) for n = 0, 1, ..., 7
x_n = np.sin(2 * np.pi * f1 * n * T) + 0.5 * np.sin(2 * np.pi * f2 * n * T + 3 * np.pi / 4)
print("The sample inputs: ", x_n)

# Calculate the 8-point DFT using the formula
X_m = np.zeros(N, dtype=complex)
for m in range(N):
    for k in range(N):
        X_m[m] += x_n[k] * np.exp(-1j * 2 * np.pi * k * m / N)

# print("The DFT outputs: ", X_m)

# Threshold to treat very small values as zero
threshold = 1e-10

# Apply thresholding and separate components for plotting
magnitude = np.abs(X_m)
phase = np.angle(X_m, deg=True)  # Phase in degrees
real_part = np.real(X_m)
imaginary_part = np.imag(X_m)

# Applying threshold to small values
magnitude = np.where(magnitude < threshold, 0, magnitude)
phase = np.where(np.abs(phase) < threshold, 0, phase)
real_part = np.where(np.abs(real_part) < threshold, 0, real_part)
imaginary_part = np.where(np.abs(imaginary_part) < threshold, 0, imaginary_part)

# Plotting in a format similar to the image provided
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Magnitude plot
axs[0, 0].stem(n, magnitude, basefmt=" ")
axs[0, 0].set_title("Magnitude of X(m)")
axs[0, 0].set_xlabel("m (kHz)")
axs[0, 0].set_ylabel("Magnitude")
axs[0, 0].set_xticks(n)

# Phase plot
axs[0, 1].stem(n, phase, basefmt=" ")
axs[0, 1].set_title("Phase of X(m), Xf(m), in deg.")
axs[0, 1].set_xlabel("m (kHz)")
axs[0, 1].set_ylabel("Phase (degrees)")
axs[0, 1].set_xticks(n)

# Real part plot
axs[1, 0].stem(n, real_part, basefmt=" ")
axs[1, 0].set_title("Real part of X(m)")
axs[1, 0].set_xlabel("m (kHz)")
axs[1, 0].set_ylabel("Real part")
axs[1, 0].set_xticks(n)

# Imaginary part plot
axs[1, 1].stem(n, imaginary_part, basefmt=" ")
axs[1, 1].set_title("Imag. part of X(m)")
axs[1, 1].set_xlabel("m (kHz)")
axs[1, 1].set_ylabel("Imaginary part")
axs[1, 1].set_xticks(n)

# Adjust layout to match format
plt.tight_layout()
plt.show()
