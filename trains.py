import sys
sys.setrecursionlimit(2001)
n = int(input())

if n < 3: 
    print(n)
    exit()

lst = [int(input()) for _ in range(n)]
def take(mn, mx, idx, curr, best):
    best = max(best, curr)
    if best >= curr + n - idx: return best
    if idx == n: return curr
    t = lst[idx]
    if mx > t and mn < t: return curr
    else: return max(take(min(mn, t), max(mx, t), idx+1, curr+1, best), take(mn, mx, idx+1, curr, best))

print(take(10000, 0, 0, 0, 2))