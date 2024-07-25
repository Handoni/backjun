import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]

d = deque()
dx,dy=[1,0,-1,0],[0,1,0,-1]

for i in range(N):
    for j in range(M):
        if array[i][j] == 1:
            d.append([i,j])

def bfs():
    while d:
        now = d.popleft()
        for di,dj in zip(dx,dy):
            i=now[0]+di
            j=now[1]+dj
            if 0<=i<N and 0<=j<M and array[i][j] == 0:
                array[i][j] = array[now[0]][now[1]] + 1
                d.append([i,j])

bfs()
res=0
for i in array:
    for j in i:
        if j == 0:
            print("-1")
            exit()
    res=max(res,max(i))
print(res-1)
