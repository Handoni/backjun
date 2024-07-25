import sys,copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline
EMPTY = 0
WALL = 1
VIRUS = 2
res = 0
diff = [[1,0],[0,1],[-1,0],[0,-1]]
N,M = map(int,input().split())

array = [list(map(int,input().split())) for _ in range(N)]
empty_list = []
virus_list = []

for i in range(N):
    for j in range(M):
        if array[i][j] == EMPTY:
            empty_list.append((j,i))
        elif array[i][j] == VIRUS:
            virus_list.append((j,i))

def bfs(a:list):
    d = deque()
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    global res

    for v in virus_list:
        d.append(v)
    while d:
        cur_x,cur_y = d.popleft()
        for dx,dy in diff:
            nx = cur_x+dx
            ny = cur_y+dy
            if 0<=nx<M and 0<=ny<N and a[ny][nx] == EMPTY and visited[ny][nx] == False:
                d.append((nx,ny))
                a[ny][nx] = VIRUS
                visited[ny][nx] = True

    for line in a:
        cnt += line.count(EMPTY)
    
    res = max(res,cnt)
    
for walls in combinations(empty_list,3):
    for x,y in walls:
        array[y][x] = WALL
    a = copy.deepcopy(array)
    bfs(a)
    for x,y in walls:
        array[y][x] = EMPTY
print(res)