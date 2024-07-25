import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
ans = [0 for _ in range(N+1)]

def bfs():
    d = deque()
    d.append(1)
    visited = [False for _ in range(N+1)]
    visited[1] = True
    
    while d:
        now=d.popleft()
        for i in graph[now]:
            if not visited[i]:
                ans[i]=now
                d.append(i)
                visited[i]=True
bfs()
for i in ans[2:]:
    print(i)