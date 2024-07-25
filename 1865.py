import sys

input = sys.stdin.readline
inf = int(1e9)


def bf(start):
    dis = [inf] * N
    dis[start] = 0

    for i in range(N):
        for cur, next, cost in edges:
            if dis[next] > cost+dis[cur]:
                dis[next] = cost+dis[cur]
                if i == N-1:
                    return True
    return False


TC = int(input().rstrip())

for ___ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S-1, E-1, T))
        edges.append((E-1, S-1, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S-1, E-1, -T))

    print("YES" if bf(0) else "NO")
