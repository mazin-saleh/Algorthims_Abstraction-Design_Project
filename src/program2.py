from typing import List, Tuple


def program2(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 2
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    if n == 0: # edge
        return 0, []
    
    chosenL = [0] * n  # list that indicates the has the maximum value using the vaults given
    helperL = [-1] * n  # list that will help me keep track if the previous vault chosen is valid considering the next one
    chosenStatus = [False] * n  # separate list that will keep track of the status of whether we chose the vault or not

    for vault in range(n):
        if vault > 0: # best value we can have is the same as the previous vault
            chosenL[vault] = chosenL[vault - 1]
            helperL[vault] = helperL[vault - 1]
        else:  # base cases
            chosenL[vault] = 0
            helperL[vault] = -1

        vaultValue = values[vault] #take the value of the current vault we're on
        if vault - k - 1 >= 0:
            vaultValue += chosenL[vault - k - 1] # if we can safely pick vault before it, add it to overall value

        # if picking the current vault is better than what we already chose, fix accordingly
        if vaultValue > chosenL[vault]:
            chosenL[vault] = vaultValue
            helperL[vault] = vault - k - 1 # set helper to the last safe vault we could've chosen
            chosenStatus[vault] = True # set boolean to true to indicate we chose this vault
        else:
            chosenStatus[vault] = False
    
    totalValue = chosenL[n-1]
    # Backtrack from the end to reconstruct the chosen indices
    finalList = []
    i = n - 1
    while i >= 0:
        if chosenStatus[i]:
            finalList.append(i + 1)
            i = helperL[i]  # jump to the previous safe index
        else:
            i -= 1
    finalList.reverse()
    return totalValue, finalList


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program2(n, k, values)

    print(m)
    for i in indices:
        print(i)
