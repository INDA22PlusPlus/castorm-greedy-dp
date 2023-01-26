import math
for _ in range(int(input())):
    N = int(input())
    V = [int(input()) for _ in range(int(input()))]

    dp = [math.inf for _ in range(20001)] 
    dp[0] = 0
    
    for C in V:
        for v in [i for i in range(20000 - C)][::-1]:
            if dp[v] < math.inf:
                dp[v+C] = min(dp[v+C], dp[v] + 1)

    for i in range(N, 20001):
        if dp[i] != math.inf:
            print(i, dp[i])
            break
    else:
        print(sum(V), len(V))