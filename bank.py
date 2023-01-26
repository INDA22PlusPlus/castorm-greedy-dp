def f():return tuple(map(int,input().split()))
N,T=f();p,t,s,x=sorted([f() for _ in range(N)]),0,0,[]
while p and t<=T:
 c,d=p.pop()
 for i in range(d+1):
  if d-i not in x:x.append(d-i);s+=c;t+=1;break
print(s)
