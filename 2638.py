import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush

N, M = map(int, input().split())
t=0
G = [list(map(int, input().split())) for _ in range(N)]

d = [(0,-1), (-1,0), (1,0), (0,1)]

q = []

visited = [[False for _ in range(M)] for __ in range(N)]

for x in range(M):
    heappush(q, (0,x,0))
    visited[0][x] = True
    heappush(q, (0,x,N-1))
    visited[N-1][x] = True

for y in range(1,N-1):
    heappush(q, (0,0,y))
    visited[y][0] = True
    heappush(q, (0,M-1,y))
    visited[y][M-1] = True

while q:
    t, x, y = heappop(q)
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < M and 0 <= ny < N):
            continue
        if visited[ny][nx]:
            continue
        if G[ny][nx] == 0:
            visited[ny][nx] = True
            heappush(q,(t,nx,ny))
        elif G[ny][nx] == 1:
            G[ny][nx] += 1
        elif G[ny][nx] == 2:
            visited[ny][nx] = True
            G[ny][nx] = 0
            heappush(q,(t+1, nx, ny))

print(t)