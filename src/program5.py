from typing import List, Tuple


def program5(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 5
    
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

    dp = [0] * n
    dp[0] = values[0] #initialize dp list, this will be the running total of the best values


    for i in range(1,n): 
        if i-k-1 >= 0: 
            dp[i] = max(dp[i-1], dp[i-k-1] + values[i])
        else:
            dp[i] = max(dp[i-1], values[i])

    # RECONSTRUCTION #
    while vault >= 0:
        if vault-k-1 >= 0: #if vaults exist -k positions away from the current vault
            if dp[vault] == dp[vault-k-1] + values[vault]: #if the current addition of vaults equals the addition of the current one alongside the previous i-k-1 vaults
                vaultsChosen.append(vault + 1)
                vault = vault-k-1
            else:
                vault -= 1
        else: #if not and the current vault equals the same value as the greatest running total, just break and add the singular vault to the list
            if dp[vault] == values[vault]:
                vaultsChosen.append(vault + 1)
                break
            else: 
                vault -= 1

    return dp[n-1], vaultsChosen[::-1] 


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program5(n, k, values)

    print(m)
    for i in indices:
        print(i)
