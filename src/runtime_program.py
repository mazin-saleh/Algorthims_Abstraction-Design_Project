import random
import time
import matplotlib.pyplot as plt
from program1 import program1
from program2 import program2
import numpy as np

# Parameters
k = 5
sizes = [10000, 20000, 30000, 40000, 50000]

# Function to get averaged timing over 3 runs to smooth microsecond noise
def average_runtime(func, n, k, values):
    runs = []
    for _ in range(3):  # Run three times
        start = time.perf_counter()
        func(n, k, values)
        end = time.perf_counter()
        runs.append(end - start)
    return np.mean(runs)

# ---------- Program 1 (S1) ----------
times_s1 = []
for n in sizes:
    values = sorted(random.randint(1, 100000) for _ in range(n))
    avg_time = average_runtime(program1, n, k, values)
    times_s1.append(avg_time)
    print(f"S1 | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7, 5))
plt.plot(sizes, times_s1, 'b-s', linewidth=2, label='Program 1 (S1)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))  # use scientific notation (e.g., ·10⁻³)
plt.title("Running Time vs Number of Elements — Program 1 (S1)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program1_runtime.png", dpi=300)
plt.close()

# ---------- Program 2 (S2) ----------
times_s2 = []
for n in sizes:
    half = n // 2
    left = sorted(random.randint(1, 50000) for _ in range(half))[::-1]
    right = sorted(random.randint(1, 50000) for _ in range(n - half))
    values = left + right

    avg_time = average_runtime(program2, n, k, values)
    times_s2.append(avg_time)
    print(f"S2 | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7, 5))
plt.plot(sizes, times_s2, 'r-o', linewidth=2, label='Program 2 (S2)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
plt.title("Running Time vs Number of Elements — Program 2 (S2)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program2_runtime.png", dpi=300)
plt.close()

print("\n✅ Saved polished plots:")
print(" - program1_runtime.png")
print(" - program2_runtime.png")
