import math
for _ in range(int(input())):
    N = int(input())
    V = [int(input()) for _ in range(int(input()))]
    dp = [math.inf for _ in range(N * 2 + 1)] 
    dp[0] = 0
    for i in range(1, N * 2 + 1):
        for v in V:
            idx = i - v
            if idx < 0: continue
            dp[i] = min(dp[idx] + 1, dp[i])
    for i in range(N, N * 2 + 1):
        if dp[i] != math.inf:
            print(i, dp[i])
            break
    else:
        print(sum(V), len(V))