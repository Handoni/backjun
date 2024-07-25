import sys
from collections import deque
from math import inf
input = sys.stdin.readline

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(s:int):
    d=deque()
    d.append((s,0))
    visited=[s]
    cnt=0
    
    while d:
        now=d.popleft()
        n=now[0]
        v=now[1]
        cnt+=v
        
        for i in graph[n]:
            if i not in visited:
                d.append((i,v+1))
                visited.append(i)
                
    return cnt
num=inf

for i in range(1,N+1):
    b=bfs(i)
    if b<num:
        res=i
        num=b
print(res)