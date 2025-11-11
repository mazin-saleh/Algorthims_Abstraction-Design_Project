from typing import List, Tuple


def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 4B
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    if n == 0: # base case
        return 0, []
    
    vaultsChosen = [] # return list (reconstruction)
    vault = n-1 # index for reconstruction purposes

    dp = [] * n, dp[0] = values[0] #initialize dp list, this will be the running total of the best values

    # Solution to CASE 1 and CASE 2
    # CASE 1: if we take i
        # if vaults exist past -k, take i and i-k-1
        # if vaults don't exist past -k, just take i
    # CASE 2: if we don't take i
        # if we don't decide to take i, then we would just take the last total value which we know is the best as of yet

    for currentVault in range(1,n):
        dp[currentVault] = dp[currentVault - 1]
        
        for validVault in range(currentVault):
            if currentVault - validVault > k: 
                dp[currentVault] = max(dp[currentVault], dp[validVault] + values[currentVault])

        dp[currentVault] = max(dp[currentVault], values[currentVault]

    
    # RECONSTRUCTION #
    while vault >= 0:
        if vault-k-1 >= 0: #if vaults exist -k positions away from the current vault
            if dp[vault] == dp[vault-k-1] + values[vault]: #if the current addition of vaults equals the addition of the current one alongside the previous i-k-1 vaults
                vaultsChosen.append(vault)
                vault = vault-k-1
            else:
                vault -= 1
        else: #if not and the current vault equals the same value as the greatest running total, just break and add the singular vault to the list
            if dp[vault] == values[vault]:
                vaultsChosen.append(vault)
                break
            else: 
                vault -= 1


    return dp[n-1], vaultsChosen[::-1]


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4B(n, k, values)

    print(m)
    for i in indices:
        print(i)
