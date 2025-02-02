def minCost(cost: list[int]) -> int:
    n = len(cost)
    prev1, prev2 = 0, 0

    for i in range(2, n+1):
        curr = min(prev1 + curr[i - 1], prev2 + curr[i - 2])
        prev2 = prev1
        prev1 = curr
    
    return prev1