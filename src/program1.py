from typing import List, Tuple


def program1(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 1
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    
    chosen_indices = []  # This will store the vault indices we decide to choose
    
    # Start from the last vault and work backwards
    i = n - 1

    # Keep going until we've checked all vaults
    while i >= 0:
        # Add this vault to our selection
        chosen_indices.append(i)
        
        # Skip the next k vaults to satisfy the distance constraint
        i -= (k + 1)

    # Since we built the list backwards, we need to reverse it to get the correct order
    chosen_indices.reverse()
    
    # Now calculate the total value and convert indices to 1-based
    total = 0  # Running sum of all values from chosen vaults
    out_indices = []  # Final list of 1-indexed vault positions

    # Go through each vault we chose
    for idx in chosen_indices:
        # Add its value to our total score
        total += values[idx]
        # Convert from 0-indexed to 1-indexed for the output format
        out_indices.append(idx + 1)

    return total, out_indices

if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program1(n, k, values)

    print(m)
    for i in indices:
        print(i)