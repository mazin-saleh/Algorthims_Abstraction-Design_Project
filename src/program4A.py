from typing import List, Tuple
from functools import lru_cache

def program4A(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """ 
    Solution to Program 4A

    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults
    
    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    
    # Keep track of which vault we came from so we can backtrack later
    parent = [-1] * n

    @lru_cache(maxsize=None)
    def dp_end(i: int) -> int:
        # Figure out the last vault we could've picked before this one
        last_allowed = i - (k + 1)
        best_prev_val = 0
        best_prev_idx = -1

        # Check all the vaults we could've come from and find the best one
        j = 0
        while j <= last_allowed:
            val_j = dp_end(j)
            if val_j > best_prev_val:
                best_prev_val = val_j
                best_prev_idx = j
            j += 1

        # Remember which previous vault gave us the best result
        parent[i] = best_prev_idx
        return values[i] + best_prev_val

    if n == 0:
        return 0, []

    # Try ending at each vault and see which one gives the max total
    best_total = -1
    best_idx = -1
    for i in range(n):
        cur = dp_end(i)
        if cur > best_total:
            best_total = cur
            best_idx = i

    # Work backwards from the best ending vault to build our answer
    chosen = []
    i = best_idx
    while i != -1:
        chosen.append(i + 1)  # convert to 1-based
        i = parent[i]

    chosen.reverse()  # flip it so indices are in order
    return best_total, chosen


# wrapper for external callers/tests
def solve(values: List[int], k: int) -> Tuple[int, List[int]]:
    return program4A(len(values), k, values)


# wrapper for demo/tests (n, k, values signature)
def solve(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    return program4A(n, k, values)


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4A(n, k, values)

    print(m)
    for i in indices:
        print(i)