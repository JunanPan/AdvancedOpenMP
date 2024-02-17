import matplotlib.pyplot as plt

# Matrix sizes for reference
sizes = [32, 64, 96, 128, 160, 192, 224, 256]

# Performance metrics (from OMP_PLACES=sockets experiment)
new_base = [1968.64, 2098.52, 3740.96, 3426.6, 1913.44, 3507.6, 3712.32, 3414.24]

# Performance metrics with OMP_PLACES=cores and various OMP_PROC_BIND settings
cores_true = [1605.36, 2053.24, 4542.78, 4269.34, 5138.56, 5523.94, 5315.54, 5192.08]
cores_close = [1687.56, 2005.44, 4339.46, 4234.96, 4247.52, 6828.92, 5118.84, 6486.32]
cores_spread = [1688.04, 1695.64, 2644.54, 2413.64, 5395.88, 3092.04, 2978.08, 2782.26]

# Recalculating the speedup of cores_true, cores_close, and cores_spread over the new baseline
new_speedup_cores_true = [b/t for b, t in zip(new_base, cores_true)]
new_speedup_cores_close = [b/c for b, c in zip(new_base, cores_close)]
new_speedup_cores_spread = [b/s for b, s in zip(new_base, cores_spread)]

# Plotting the speedup for different OMP_PROC_BIND settings with OMP_PLACES=cores against the new baseline
plt.figure(figsize=(10, 6))
plt.plot(sizes, new_speedup_cores_true, label='OMP_PROC_BIND=true', marker='o')
plt.plot(sizes, new_speedup_cores_close, label='OMP_PROC_BIND=close', marker='o')
plt.plot(sizes, new_speedup_cores_spread, label='OMP_PROC_BIND=spread', marker='o')

plt.xlabel('Matrix Size')
plt.ylabel('Speedup Over New Base (OMP_PLACES=sockets)')
plt.title('Speedup of Different OMP_PROC_BIND Settings With New Base')
plt.legend()
plt.grid(True)
plt.xticks(sizes)
plt.show()
