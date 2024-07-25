import heapq, sys

input = sys.stdin.readline

N = int(input().rstrip())

heap = []

for _ in range(N):
    x = int(input().rstrip())
    if x==0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(x),x))