import math
import matplotlib.pyplot as plt

def find_and_plot_sequences(N, max_m=None):
    if max_m is None:
        max_m = int(math.isqrt(2*N)) + 2

    solutions = []

    for m in range(1, max_m + 1):
        numerator = N - m*(m-1)
        if numerator < 0:
            break

        if numerator % m == 0:
            s = numerator // m
            if s > 0 and s % 2 == 1:
                end = s + 2*(m-1)
                solutions.append((m, s, end))

    if solutions:
        ms = [sol[0] for sol in solutions]
        ss = [sol[1] for sol in solutions]

        plt.scatter(ms, ss)
        plt.xlabel('m (number of consecutive odds)')
        plt.ylabel('s (starting odd number)')
        plt.title(f'All solutions for N={N} (searched m up to {max_m})')
        plt.show()

        print(f"Found {len(solutions)} solutions for N={N}:")
        for (m_val, s_val, e_val) in solutions:
            print(f"  m={m_val}, s={s_val}, e={e_val}  =>  sum of {m_val} consecutive odds from {s_val} to {e_val}")
    else:
        print(f"No solutions found for N={N} up to m={max_m}.")

# Example usage:
N = 6757
find_and_plot_sequences(N)
