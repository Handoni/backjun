from collections import deque
N, M = map(int, input().split())

G = []
A = []

for i in range(N):
    temp = list(map(int,input().split()))
    if 2 in temp:
        start = (temp.index(2), i)
    G.append(temp)
    temp2 = temp.copy()
    for j in range(len(temp2)):
        if temp2[j] == 1:
            temp2[j] = -1
    A.append(temp2)
A[start[1]][start[0]] = 0

q = deque()
q.append(start)
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not ( 0 <= nx < M and 0 <= ny < N): continue
        if not A[ny][nx] == -1: continue
        if G[ny][nx] == 1:
            A[ny][nx] = A[y][x] + 1
            q.append((nx,ny))


for line in A:
    for item in line:
        print(item, end=' ')
    print()