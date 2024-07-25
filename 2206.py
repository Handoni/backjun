import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
array = [list(map(int, input().rstrip())) for _ in range(N)]


def bfs():
    diff = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    d = deque()
    d.append((0, 0, 0))  # breaked,x,y
    visited = [[[0]*M for _ in range(N)] for __ in range(2)]
    visited[0][0][0] = 1

    while d:
        breaked, x, y = d.popleft()

        if x == M-1 and y == N-1:
            return visited[breaked][y][x]
        for dx, dy in diff:
            nx, ny = x+dx, y+dy

            if 0 <= nx < M and 0 <= ny < N:
                if array[ny][nx] == 0 and not visited[breaked][ny][nx]:
                    d.append((breaked, nx, ny))
                    visited[breaked][ny][nx] = visited[breaked][y][x] + 1
                elif breaked == 0:
                    d.append((1, nx, ny))
                    visited[1][ny][nx] = visited[0][y][x] + 1
    return -1


print(bfs())
