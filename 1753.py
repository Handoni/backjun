import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
K = int(input().rstrip())
dp = [INF]*(V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
heap=[]
def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))
    
    while heap:
        weight, now = heapq.heappop(heap)
        
        if dp[now] < weight:
            continue
        
        for w, next in graph[now]:
            next_weight = w+weight
            
            if next_weight < dp[next]:
                dp[next] = next_weight
                heapq.heappush(heap,(next_weight,next))

Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])