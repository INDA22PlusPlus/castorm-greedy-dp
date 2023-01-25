N, T = map(int, input().split())
people = []
for i in range(N):
    c, t = map(int, input().split())
    people.append((c,t))
    
t = 0

people.sort(key=lambda x: -(x[0] * 48 - x[1]))
res = [None for _ in range(T + 1)]
while people and t <= T:
    curr = people.pop(0)
    for i in range(curr[1] + 1):
        if res[curr[1] - i] == None:
            res[curr[1] - i] = curr[0]
            t += 1
            break
tot = 0
for i in res:
    if i != None: tot += i
print(tot)