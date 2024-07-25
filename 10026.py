import sys
import copy
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(N)]
graph2 = copy.deepcopy(graph)
diff = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs1(x: int, y: int, char: str):
    d = deque()
    d.append((x, y))
    graph[y][x] = 0
    while d:
        now_x, now_y = d.popleft()
        for dx, dy in diff:
            nx, ny = now_x+dx, now_y+dy
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == char:
                d.append((nx, ny))
                graph[ny][nx] = 0


def bfs2(x: int, y: int, char: str):
    d = deque()
    d.append((x, y))
    graph2[y][x] = 0
    while d:
        now_x, now_y = d.popleft()
        for dx, dy in diff:
            nx, ny = now_x+dx, now_y+dy
            if 0 <= nx < N and 0 <= ny < N and graph2[ny][nx] != 0:
                if graph2[ny][nx] in ['R', 'G'] and char in ['R', 'G']:
                    d.append((nx, ny))
                    graph2[ny][nx] = 0
                elif graph2[ny][nx] == char:
                    d.append((nx, ny))
                    graph2[ny][nx] = 0


cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            bfs1(j, i, graph[i][j])
            cnt1 += 1
        if graph2[i][j] != 0:
            bfs2(j, i, graph2[i][j])
            cnt2 += 1

print(cnt1, cnt2)
