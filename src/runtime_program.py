# import random
# import time
# import matplotlib.pyplot as plt
# from program1 import program1
# from program2 import program2
# import numpy as np

# # Parameters
# k = 5
# sizes = [10000, 20000, 30000, 40000, 50000]

# # Function to get averaged timing over 3 runs to smooth microsecond noise
# def average_runtime(func, n, k, values):
#     runs = []
#     for _ in range(3):  # Run three times
#         start = time.perf_counter()
#         func(n, k, values)
#         end = time.perf_counter()
#         runs.append(end - start)
#     return np.mean(runs)

# # ---------- Program 1 (S1) ----------
# times_s1 = []
# for n in sizes:
#     values = sorted(random.randint(1, 100000) for _ in range(n))
#     avg_time = average_runtime(program1, n, k, values)
#     times_s1.append(avg_time)
#     print(f"S1 | n={n} | avg_time={avg_time:.6f}s")

# plt.figure(figsize=(7, 5))
# plt.plot(sizes, times_s1, 'b-s', linewidth=2, label='Program 1 (S1)')
# plt.xlabel("Number of Elements", fontsize=12)
# plt.ylabel("Running Time (seconds)", fontsize=12)
# plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))  # use scientific notation (e.g., ·10⁻³)
# plt.title("Running Time vs Number of Elements — Program 1 (S1)", fontsize=13)
# plt.legend()
# plt.grid(True, linestyle="--", alpha=0.3)
# plt.tight_layout()
# plt.savefig("program1_runtime.png", dpi=300)
# plt.close()

# # ---------- Program 2 (S2) ----------
# times_s2 = []
# for n in sizes:
#     half = n // 2
#     left = sorted(random.randint(1, 50000) for _ in range(half))[::-1]
#     right = sorted(random.randint(1, 50000) for _ in range(n - half))
#     values = left + right

#     avg_time = average_runtime(program2, n, k, values)
#     times_s2.append(avg_time)
#     print(f"S2 | n={n} | avg_time={avg_time:.6f}s")

# plt.figure(figsize=(7, 5))
# plt.plot(sizes, times_s2, 'r-o', linewidth=2, label='Program 2 (S2)')
# plt.xlabel("Number of Elements", fontsize=12)
# plt.ylabel("Running Time (seconds)", fontsize=12)
# plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
# plt.title("Running Time vs Number of Elements — Program 2 (S2)", fontsize=13)
# plt.legend()
# plt.grid(True, linestyle="--", alpha=0.3)
# plt.tight_layout()
# plt.savefig("program2_runtime.png", dpi=300)
# plt.close()

# print("\n Saved polished plots:")
# print(" - program1_runtime.png")
# print(" - program2_runtime.png")


import random
import time
import matplotlib.pyplot as plt
import numpy as np
from program1 import program1
from program2 import program2
from program3 import program3
from program4A import program4A
from program4B import program4B
from program5 import program5

# -----------------------------
# Parameters
# -----------------------------
k = 5
sizes = [10000, 20000, 30000, 40000, 50000]

# Average runtime helper (3 runs)
def average_runtime(func, n, k, values):
    runs = []
    for _ in range(3):
        start = time.perf_counter()
        func(n, k, values)
        end = time.perf_counter()
        runs.append(end - start)
    return np.mean(runs)

# -----------------------------
# Program 1 (S1)
# -----------------------------
times_s1 = []
for n in sizes:
    values = sorted(random.randint(1, 100000) for _ in range(n))
    avg_time = average_runtime(program1, n, k, values)
    times_s1.append(avg_time)
    print(f"S1 | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7,5))
plt.plot(sizes, times_s1, 'b-s', linewidth=2, label='Program 1 (S1)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Running Time vs Number of Elements — Program 1 (S1)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program1_runtime.png", dpi=300)
plt.close()

# -----------------------------
# Program 2 (S2)
# -----------------------------
times_s2 = []
for n in sizes:
    half = n // 2
    left = sorted(random.randint(1, 50000) for _ in range(half))[::-1]
    right = sorted(random.randint(1, 50000) for _ in range(n - half))
    values = left + right
    avg_time = average_runtime(program2, n, k, values)
    times_s2.append(avg_time)
    print(f"S2 | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7,5))
plt.plot(sizes, times_s2, 'r-o', linewidth=2, label='Program 2 (S2)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Running Time vs Number of Elements — Program 2 (S2)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program2_runtime.png", dpi=300)
plt.close()

# -----------------------------
# Program 3 (Brute Force G)
# -----------------------------
times_s3 = []
# use small explicit sizes for brute force to avoid recursion depth and time blowup
for n in [12, 15, 18, 20]:
    values = [random.randint(1, 1000) for _ in range(n)]
    avg_time = average_runtime(program3, n, k, values)
    times_s3.append(avg_time)
    print(f"S3 | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7,5))
plt.plot(sizes[:4], times_s3, 'g-^', linewidth=2, label='Program 3 (Brute Force G)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Running Time vs Number of Elements — Program 3 (Brute Force G)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program3_runtime.png", dpi=300)
plt.close()

# -----------------------------
# Program 4A (DP for G)
# -----------------------------
times_s4a = []
for n in sizes:
    values = [random.randint(1, 1000) for _ in range(n)]
    avg_time = average_runtime(program4A, n, k, values)
    times_s4a.append(avg_time)
    print(f"S4A | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7,5))
plt.plot(sizes, times_s4a, 'm-D', linewidth=2, label='Program 4A (DP for G)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Running Time vs Number of Elements — Program 4A (DP for G)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program4A_runtime.png", dpi=300)
plt.close()

# -----------------------------
# Program 4B (DP for S2)
# -----------------------------
times_s4b = []
for n in sizes:
    half = n // 2
    left = sorted(random.randint(1, 50000) for _ in range(half))[::-1]
    right = sorted(random.randint(1, 50000) for _ in range(n - half))
    values = left + right
    avg_time = average_runtime(program4B, n, k, values)
    times_s4b.append(avg_time)
    print(f"S4B | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7,5))
plt.plot(sizes, times_s4b, 'c-p', linewidth=2, label='Program 4B (DP for S2)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Running Time vs Number of Elements — Program 4B (DP for S2)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program4B_runtime.png", dpi=300)
plt.close()

# -----------------------------
# Program 5 (DP Quality Comparison)
# -----------------------------
times_s5 = []
for n in sizes:
    values = [random.randint(1, 100000) for _ in range(n)]
    avg_time = average_runtime(program5, n, k, values)
    times_s5.append(avg_time)
    print(f"S5 | n={n} | avg_time={avg_time:.6f}s")

plt.figure(figsize=(7,5))
plt.plot(sizes, times_s5, 'y-*', linewidth=2, label='Program 5 (DP Quality Metric)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Running Time vs Number of Elements — Program 5 (DP Quality Metric)", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program5_runtime.png", dpi=300)
plt.close()

# -----------------------------
# Overlay Plots (All 3–5)
# -----------------------------
plt.figure(figsize=(7,5))
plt.plot(sizes[:4], times_s3, 'g-^', linewidth=2, label='Program 3 (Brute Force)')
plt.plot(sizes, times_s4a, 'm-D', linewidth=2, label='Program 4A (DP G)')
plt.plot(sizes, times_s4b, 'c-p', linewidth=2, label='Program 4B (DP S2)')
plt.plot(sizes, times_s5, 'y-*', linewidth=2, label='Program 5 (DP Quality)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.title("Runtime Comparison of Programs 3–5", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program3to5_overlay.png", dpi=300)
plt.close()

# -----------------------------
# Overlay Plots (4A vs 4B)
# -----------------------------
plt.figure(figsize=(7,5))
plt.plot(sizes, times_s4a, 'm-D', linewidth=2, label='Program 4A (DP G)')
plt.plot(sizes, times_s4b, 'c-p', linewidth=2, label='Program 4B (DP S2)')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Running Time (seconds)", fontsize=12)
plt.title("Comparison of Programs 4A and 4B", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("program4A_4B_overlay.png", dpi=300)
plt.close()

# -----------------------------
# Quality Comparison Plot (Algorithm 1 vs others)
# -----------------------------
hg = np.array(times_s1[:len(times_s3)])  # greedy
ho = np.array(times_s3)                  # brute-force
quality = (hg - ho) / ho
plt.figure(figsize=(7,5))
plt.plot(sizes[:len(quality)], quality, 'r--o', linewidth=2, label='(hg - ho)/ho')
plt.xlabel("Number of Elements", fontsize=12)
plt.ylabel("Relative Quality Metric", fontsize=12)
plt.title("Output Quality Comparison", fontsize=13)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("quality_comparison.png", dpi=300)
plt.close()

print("\n Saved polished plots:")
print(" - program1_runtime.png")
print(" - program2_runtime.png")
print(" - program3_runtime.png")
print(" - program4A_runtime.png")
print(" - program4B_runtime.png")
print(" - program5_runtime.png")
print(" - program3to5_overlay.png")
print(" - program4A_4B_overlay.png")
print(" - quality_comparison.png")
