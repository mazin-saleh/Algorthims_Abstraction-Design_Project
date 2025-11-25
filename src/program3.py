from typing import List, Tuple


def program3(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Brute-force recursive solution.
    """
    best_total = 0
    best_set: List[int] = []

    def explore(i: int, current_total: int, current_set: List[int]):
        nonlocal best_total, best_set

        if i >= n:
            if current_total > best_total:
                best_total = current_total
                best_set = current_set.copy()
            return

        # Option 1: skip current vault
        explore(i + 1, current_total, current_set)

        # Option 2: take current vault
        explore(i + k + 1, current_total + values[i], current_set + [i])

    explore(0, 0, [])

    # Convert to 1-based
    output_indices = [x + 1 for x in best_set]
    return best_total, output_indices


# ===============================================================
# ONLY ONE solve() — correct signature for the demo
# ===============================================================
def solve(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    return program3(n, k, values)


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program3(n, k, values)

    print(m)
    for i in indices:
        print(i)
