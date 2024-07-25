from collections import deque
N, K = map(int, input().split())


def bfs():
    d = deque()
    d.append((N, 0))
    visited = set()
    visited.add(N)
    while d:
        now, time = d.popleft()
        if now == K:
            return time
        if 0 <= now-1 <= 100001 and now-1 not in visited:
            d.append((now-1, time+1))
            visited.add(now-1)
        if 0 <= now*2 <= 100001 and now*2 not in visited:
            d.appendleft((now*2, time))
            visited.add(now*2)
        if 0 <= now+1 <= 100001 and now+1 not in visited:
            d.append((now+1, time+1))
            visited.add(now+1)


print(bfs())
