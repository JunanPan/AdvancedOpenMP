import matplotlib.pyplot as plt

# Matrix sizes for reference
sizes = [32, 64, 96, 128, 160, 192, 224, 256]

# Updated base performance metrics
base_performance = [1968.64, 2098.52, 3740.96, 3426.6, 1913.44, 3507.6, 3712.32, 3414.24]

# Performance metrics with OMP_PLACES=sockets and various OMP_PROC_BIND settings
sockets_true_performance = [1548.56, 1991.00, 3616.92, 3949.92, 4525.54, 5605.22, 3873.72, 3500.70]
sockets_close_performance = [2087.18, 2567.62, 3850.28, 3869.42, 4749.78, 5624.40, 4856.58, 5523.82]
sockets_spread_performance = [1614.44, 1640.72, 2633.42, 3854.94, 7027.44, 5553.54, 4645.94, 3218.28]

# Calculating speedup over updated base performance
speedup_sockets_true = [base/socket for base, socket in zip(base_performance, sockets_true_performance)]
speedup_sockets_close = [base/socket for base, socket in zip(base_performance, sockets_close_performance)]
speedup_sockets_spread = [base/socket for base, socket in zip(base_performance, sockets_spread_performance)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, speedup_sockets_true, label='OMP_PROC_BIND=true', marker='o')
plt.plot(sizes, speedup_sockets_close, label='OMP_PROC_BIND=close', marker='o')
plt.plot(sizes, speedup_sockets_spread, label='OMP_PROC_BIND=spread', marker='o')

plt.xlabel('Matrix Size')
plt.ylabel('Speedup Over Updated Base (OMP_PLACES=sockets)')
plt.title('Speedup of Different OMP_PROC_BIND Settings With OMP_PLACES=sockets')
plt.legend()
plt.grid(True)
plt.xticks(sizes)
plt.show()
