import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    distances = [INF for _ in range(N+1)]
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, currunt = heapq.heappop(q)
        if distances[currunt] < dist:
            continue
        for next, n_dist in graph[currunt]:
            cost = dist + n_dist

            if distances[next] > cost:
                distances[next] = cost
                heapq.heappush(q, (cost, next))
    return distances


v1, v2 = map(int, input().split())

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path_v1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]  # 1->v1->v2->N
path_v2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]  # 1->v2->v1->N

res = min(path_v1, path_v2)
print(res if res < INF else -1)
