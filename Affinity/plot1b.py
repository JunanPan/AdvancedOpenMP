import matplotlib.pyplot as plt

# Matrix sizes for reference
sizes = [32, 64, 96, 128, 160, 192, 224, 256]

# Base performance metrics from the latest experiment
base_cores = [1952.92, 1875.14, 2735.26, 3915.74, 2379.72, 3386.54, 2282.52, 2799.14]

# Performance metrics with OMP_PLACES=cores
cores_true = [1605.36, 2053.24, 4542.78, 4269.34, 5138.56, 5523.94, 5315.54, 5192.08]
cores_close = [1687.56, 2005.44, 4339.46, 4234.96, 4247.52, 6828.92, 5118.84, 6486.32]
cores_spread = [1688.04, 1695.64, 2644.54, 2413.64, 5395.88, 3092.04, 2978.08, 2782.26]

# Calculating the speedup of cores_true, cores_close, and cores_spread over the base_cores
speedup_cores_true = [b/t for b, t in zip(base_cores, cores_true)]
speedup_cores_close = [b/c for b, c in zip(base_cores, cores_close)]
speedup_cores_spread = [b/s for b, s in zip(base_cores, cores_spread)]

# Plotting the speedup for different OMP_PROC_BIND settings with OMP_PLACES=cores
plt.figure(figsize=(10, 6))
plt.plot(sizes, speedup_cores_true, label='OMP_PROC_BIND=true', marker='o')
plt.plot(sizes, speedup_cores_close, label='OMP_PROC_BIND=close', marker='o')
plt.plot(sizes, speedup_cores_spread, label='OMP_PROC_BIND=spread', marker='o')

plt.xlabel('Matrix Size')
plt.ylabel('Speedup Over Base (OMP_PLACES=cores)')
plt.title('Speedup of Different OMP_PROC_BIND Settings With OMP_PLACES=cores')
plt.legend()
plt.grid(True)
plt.xticks(sizes)
plt.show()
