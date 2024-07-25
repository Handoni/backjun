from collections import deque

A, B = map(int, input().split())


def bfs():
    d = deque()
    d.append((A, 0))
    visited = set()
    visited.add(A)

    while d:
        now, dist = d.pop()
        if now == B:
            return dist+1
        if now*2 <= 10**9 and now*2 not in visited:
            d.append((now*2, dist+1))
        if now*10+1 <= 10**9 and now*10+1 not in visited:
            d.append((now*10+1, dist+1))
    return -1


print(bfs())
