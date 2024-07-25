import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
array = []

for i in range(N):
    array.append(list(map(int, input().split())))
    if 9 in array[i]:
        y = i
        x = array[i].index(9)
        array[y][x] = 0


dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]


def bfs():
    size = 2
    eaten = 0
    time = 0
    res_time = 0
    d = deque()
    d.append((x, y))
    visited = [(x, y)]

    while d:
        if d:
            d = deque(sorted(d, key=lambda x: [x[1], x[0]]))
        flag = False
        for _ in range(len(d)):
            cur_x, cur_y = d.popleft()
            if 0 < array[cur_y][cur_x] < size:
                eaten += 1
                if size == eaten:
                    size += 1
                    eaten = 0
                res_time = time
                array[cur_y][cur_x] = 0
                visited = [(cur_x, cur_y)]
                d = deque()
                flag = True

            for di, dj in zip(dy, dx):
                nx = cur_x + dj
                ny = cur_y + di
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    if array[ny][nx] <= size:
                        d.append((nx, ny))
                        visited.append((nx, ny))

            if flag:
                flag = False
                break
        time += 1
    return res_time


print(bfs())
