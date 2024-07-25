import sys
from collections import deque

input = sys.stdin.readline

M,N,H = map(int,input().split())

graph = [[list(map(int,input().split())) for _ in range(N)] for __ in range(H)]

diff = [[0,0,1],[0,0,-1],[1,0,0],[0,1,0],[-1,0,0],[0,-1,0]]

d = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                d.append((x,y,z))

def bfs():
    while d:
        x,y,z = d.popleft()
        for dx,dy,dz in diff:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and graph[nz][ny][nx]== 0:
                d.append((nx,ny,nz))
                graph[nz][ny][nx] = graph[z][y][x] + 1
            
bfs()

res=0
for layer in graph:
    for line in layer:
        if 0 in line:
            print(-1)
            exit()
        res = max(res,max(line))
print(res-1)