import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

array = [0 for _ in range(101)]

for _ in range(N):
    x,y=map(int,input().split())
    array[x]=y
for _ in range(M):
    u,v=map(int,input().split())
    array[u]=v
    
def bfs():
    d = deque()
    d.append((1,0))
    visited=set()
    visited.add(1)
    
    while d:
        n, k = d.popleft()
        if n == 100:
            return(k)
        for i in range(1,7):
            if 1<=n+i<=100:
                if array[n+i] != 0:
                    d.append((array[n+i],k+1))
                    visited.add(array[n+i])
                elif n+i not in visited:
                    d.append((n+i,k+1))
                    visited.add(n+i)
                    
print(bfs())