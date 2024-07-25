import heapq
from collections import defaultdict

N, M, X = map(int, input().split())
INF = float('inf')
G = defaultdict(lambda:defaultdict(int))
for _ in range(M):
    s, e, t = map(int, input().split())
    G[s][e] = t

def dijkstra(start, end):
    d = {node: INF for node in G}
    d[start] = 0
    q = []
    heapq.heappush(q, (d[start], start))
    
    while q:
        now_distance, now_destination = heapq.heappop(q)

        if d[now_destination] < now_distance:
            continue

        for next_destination, next_distance in G[now_destination].items():
            distance = now_distance + next_distance
            if distance < d[next_destination]:
                d[next_destination] = distance
                heapq.heappush(q, (distance, next_destination))
    return d[end]

res = -1
for i in range(1,N+1):
    res = max(res, dijkstra(i, X) + dijkstra(X, i))

print(res)