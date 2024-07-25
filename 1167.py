import sys
from collections import deque

V = int(input().rstrip())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    u = temp[0]
    for v, w in zip(temp[1::2], temp[2::2]):
        graph[u].append((v, w))


def dfs(root):
    d = deque()
    d.append((root, 0))
    res = 0
    node = None
    visited = [False for _ in range(V+1)]
    visited[root] = True
    while d:
        now, cnt = d.pop()
        for next, weight in graph[now]:
            if not visited[next]:
                d.append((next, cnt+weight))
                visited[next] = True
        else:
            res = max(res, cnt)
            if res == cnt:
                node = now
    return res, node


length, node = dfs(1)
print(dfs(node)[0])
