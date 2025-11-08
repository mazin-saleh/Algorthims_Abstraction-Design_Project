from typing import List, Tuple


def program3(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 3
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    best_total = 0
    best_set: List[int] = []

    # Recursive helper
    def explore(i: int, current_total: int, current_set: List[int]):
        nonlocal best_total, best_set

        # Base case: reached end of vault list
        if i >= n:
            if current_total > best_total:
                best_total = current_total
                best_set = current_set.copy()
            return

        # Option 1: skip current vault
        explore(i + 1, current_total, current_set)

        # Option 2: take current vault and jump k+1 ahead
        explore(i + k + 1, current_total + values[i], current_set + [i])

    # Start recursion from the first vault
    explore(0, 0, [])

    # Convert indices to 1-based for output
    output_indices = [x + 1 for x in best_set]
    return best_total, output_indices


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program3(n, k, values)

    print(m)
    for i in indices:
        print(i)