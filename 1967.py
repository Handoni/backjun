import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

array = [[] for _ in range(n+1)]

for _ in range(n-1):
    r, u, w = map(int, input().split())
    array[r].append((u, w))
    array[u].append((r, w))


def dfs(root):
    d = deque()
    d.append((root, 0))
    res = 0
    node = None
    visited = [False for _ in range(n+1)]
    visited[root] = True
    while d:
        now, cnt = d.pop()
        for next, weight in array[now]:
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
