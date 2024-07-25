import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(N)]
dy = [1,0,-1,0]
dx = [0,1,0,-1]

visited=[]
def bfs(i,j):
    d=deque()
    d.append((i,j))
    visited.append((i,j))
    res=0
    while d:
        ni,nj=d.popleft()
        res+=1
        for di,dj in zip(dy,dx):
            y = ni+di
            x = nj+dj
            if 0<=y<N and 0<=x<N and ((y,x) not in visited) and graph[y][x]=='1':
                d.append((y,x))
                visited.append((y,x))
    return res

ans=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]=='1' and ((i,j) not in visited):
            ans.append(bfs(i,j))
print(len(ans))
ans=sorted(ans)
for i in ans:
    print(i)