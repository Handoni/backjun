import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = sys.maxsize

N = int(input().strip())
M = int(input().strip())

nodes = defaultdict(lambda: defaultdict(lambda: INF))

for _ in range(M):
    start, end, cost = map(int, input().split())
    if nodes[start][end] > cost:
        nodes[start][end] = cost

start, end = map(int, input().split())

distances = [INF for _ in range(N+1)]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, current = heapq.heappop(q)
        if distances[current] < dist:
            continue
        for next, n_dist in nodes[current].items():
            cost = dist + n_dist
            if cost < distances[next]:
                distances[next] = cost
                heapq.heappush(q, (cost, next))


dijkstra(start)
print(distances[end])
