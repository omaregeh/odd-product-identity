import math
import matplotlib.pyplot as plt

def valid_sequences(N, max_m=None):
    if max_m is None:
        max_m = int(math.isqrt(2*N)) + 2
    results = []
    for m in range(1, max_m + 1):
        numerator = N - m*(m-1)
        if numerator < 0:
            break
        if numerator % m == 0:
            s = numerator // m
            if s > 0 and s % 2 == 1:
                results.append((N, m, s))
    return results

# Range of N values to explore
N_values = range(100, 1001, 25)
all_results = []

for N in N_values:
    all_results.extend(valid_sequences(N))

# Plot: each (m, s) colored by N
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    [r[1] for r in all_results],
    [r[2] for r in all_results],
    c=[r[0] for r in all_results],
    cmap='viridis',
    alpha=0.8
)
plt.colorbar(scatter, label='N')
plt.xlabel('m (number of odds)')
plt.ylabel('s (starting odd)')
plt.title('Valid Decompositions for N = 100 to 1000')
plt.grid(True)
plt.tight_layout()
plt.show()
