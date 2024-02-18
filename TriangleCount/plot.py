import matplotlib.pyplot as plt
import numpy as np

# Thread counts
threads = np.array([1, 2, 4, 8, 16, 32])

# Sequential version execution times (cycles) as baseline
# Assuming the smallest dataset as a representative example for sequential baseline
# sequential_cycles = np.array([19.2] * 6)  # Using small dataset time for all thread counts
times_small = np.array([19.2, 20.8, 19.2, 20.8, 27.2, 17.6])
times_medium = np.array([16.0, 17.6, 25.6, 28.8, 20.8, 17.6])
times_large = np.array([22.4, 19.2, 20.8, 19.2, 20.8, 24.0])
# Parallel version execution times (cycles) for different datasets
# Small dataset
small_parallel_cycles = np.array([1385812.8, 4546689.6, 41786657.6, 63801771.2, 125557139.2, 252361699.2])
# Medium dataset
medium_parallel_cycles = np.array([2490544.0, 7704132.8, 62018686.4, 96387374.4, 188035961.6, 321952550.4])
# Large dataset
large_parallel_cycles = np.array([4887276.8, 14513942.4, 157870288.0, 262684054.4, 495928302.4, 881261328.0])

# Speedups are calculated as sequential_cycles / parallel_cycles
# Note: This interpretation assumes lower cycles for sequential, which seems incorrect given the context.
# The actual intent might be to compare execution times, where more cycles = slower.
# These calculations are based on the provided numbers but likely do not reflect the expected speedup pattern.

small_speedup = times_small / small_parallel_cycles
medium_speedup = times_medium / medium_parallel_cycles
large_speedup = times_large / large_parallel_cycles

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(threads, small_speedup, marker='o', linestyle='-', color='b', label='Small Dataset')
plt.plot(threads, medium_speedup, marker='s', linestyle='-', color='r', label='Medium Dataset')
plt.plot(threads, large_speedup, marker='^', linestyle='-', color='g', label='Large Dataset')

plt.xlabel('Number of Threads')
plt.ylabel('Speedup')
plt.title('Speedup Over Sequential Execution')
plt.legend()
plt.grid(True)
plt.xticks(threads)

plt.show()

