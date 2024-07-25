from re import L
import sys
from collections import deque

input = sys.stdin.readline

N,M,V=map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs():
    d = deque()
    visited = []
    d.append(V)

    while d:
        now = d.pop()
        if now not in visited:
            visited.append(now)
            d.extend(sorted(graph[now],reverse=True))
    return visited

def bfs():
    d = deque()
    visited = []
    d.append(V)

    while d:
        now = d.popleft()
        if now not in visited:
            visited.append(now)
            d.extend(sorted(graph[now]))
    return visited

print(*dfs())
print(*bfs())