import sys
from collections import deque

df = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]


def bfs(start: tuple, end: tuple):
    d = deque()
    d.append(start)
    visited = [[0 for _ in range(l)] for __ in range(l)]
    cnt = 0
    while (d):
        now_x, now_y = d.popleft()
        if (now_x, now_y) == end:
            return visited[now_y][now_x]
        for dx, dy in df:
            nx, ny = now_x+dx, now_y+dy
            if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                d.append((nx, ny))
                visited[ny][nx] = visited[now_y][now_x] + 1


input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    l = int(input().rstrip())
    init = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(bfs(init, end))
