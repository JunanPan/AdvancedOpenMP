import matplotlib.pyplot as plt

# Matrix sizes
sizes = [32, 64, 96, 128, 160, 192, 224, 256]

# Baseline performance metrics
original = [1968.64, 2098.52, 3740.96, 3426.6, 1913.44, 3507.6, 3712.32, 3414.24]

# Performance metrics for different OMP_PROC_BIND settings
true_binding = [2343.3, 2238.0, 3742.92, 4927.06, 6461.86, 5198.7, 5049.06, 5073.12]
close_binding = [1972.48, 1995.7, 3100.8, 4437.54, 4935.48, 5940.14, 4766.34, 3955.3]
spread_binding = [1175.08, 2128.64, 1885.22, 2194.82, 2992.56, 2641.18, 3065.04, 3535.92]

# Calculating speedup as the ratio of original performance to each setting's performance
speedup_true = [o/t for o, t in zip(original, true_binding)]
speedup_close = [o/c for o, c in zip(original, close_binding)]
speedup_spread = [o/s for o, s in zip(original, spread_binding)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, speedup_true, label='True Binding', marker='o')
plt.plot(sizes, speedup_close, label='Close Binding', marker='o')
plt.plot(sizes, speedup_spread, label='Spread Binding', marker='o')

plt.xlabel('Matrix Size')
plt.ylabel('Speedup Over Original')
plt.title('Speedup of Different OMP_PROC_BIND Settings Over Original')
plt.legend()
plt.grid(True)
plt.xticks(sizes)
plt.show()
